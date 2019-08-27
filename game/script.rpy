
init -20 python:
    if renpy.mobile != True:
        import discord_rpc
        import time

        def readyCallback(current_user):
            print('Our user: {}'.format(current_user))

        def disconnectedCallback(codeno, codemsg):
            print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
                codeno, codemsg
            ))

        def errorCallback(errno, errmsg):
            print('An error occurred! Error {}: {}'.format(
                errno, errmsg
            ))
    if renpy.mobile == True:
        print('Disabled discord RPC. Not supported on mobile!')



label before_main_menu:
    if renpy.mobile != True:
        python:
            # Note: 'event_name': callback
            callbacks = {
                'ready': readyCallback,
                'disconnected': disconnectedCallback,
                'error': errorCallback,
            }
            discord_rpc.initialize('564432578803662848', callbacks=callbacks, log=False)
            start = time.time()
            print(start)
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
            discord_rpc.update_presence(
                **{
                    'details': 'Main Menu',
                    'start_timestamp': start,
                    'large_image_key': 'miku_logo'
                }
            )
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
return
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miku")
define p = Character("Miku's Fan")

image miku happy = "miku/miku happy.png"
image miku wave = "miku/miku wave.png"


transform my_top_left:
    xalign .1 yalign 0.2
transform my_bottom_left:
    xalign .1 yalign 0.5

init python:
    #Define and Init Python


    #Base Class
    class BaseClass(renpy.python.RevertableObject):

        def __getstate__(self):
            return vars(self).copy()

        def __setstate__(self,new_dict):
            self.__dict__.update(new_dict)

    #Player Class
    class Player(BaseClass):
        '''
        player Class
        '''

        def __init__(self):
            '''
            iniciar variáveis
            '''
            self.player_name = "Miku's Fan"
            self.choices = {}

        def set_name(self, name):
            if name.strip() != "":
                self.player_name = name

        def set_choice(self, choice, value):
            self.choices[choice] = value

        def get_choice(self, choice):
            if choice in self.choices:
                return self.choices[choice]
            else:
                return False


label start:
    if renpy.mobile != True:
        "Nice, you're playing on a PC. Discord RPC has been enabled! Look in your account :P"
        python:
            callbacks = {
                'ready': readyCallback,
                'disconnected': disconnectedCallback,
                'error': errorCallback,
            }
            discord_rpc.initialize('564432578803662848', callbacks=callbacks, log=False)
            start = time.time()
            discord_rpc.update_connection()
            discord_rpc.run_callbacks()
            discord_rpc.update_presence(
                **{
                    'details': 'Looking at Miku',
                    'state': 'Hidden away',
                    'large_image_key': 'miku_logo',
                    'start_timestamp': start
                }
            )

            discord_rpc.update_connection()
            discord_rpc.run_callbacks()

        jump intro_start
    if renpy.mobile == True:
        jump intro_start

label intro_start:
    $ the_player = Player()
    menu:
        "Did you see the credits?"
        "Yes":
            jump game_start
        "No":
            show dev eyes closed with dissolve
            "Welcome player!"
            "We know you want to start playing the game, but first. Please listen to this message."
            show mikufan at my_top_left with dissolve
            show mikufan_banner at my_bottom_left with dissolve
            "You may have downloaded the game from the Mikufan discord!"
            "These nice people helped us getting the game on their discord!"
            "Also: Please have some credit to the people that helped us to make the game as it is now:"
            "Tanix#5876 - Developer\nStefano#7366 - Developer"
            "And now, lets play the game!"
            hide dev eyes closed with dissolve
            hide mikufan at my_top_left with dissolve
            hide mikufan_banner at my_bottom_left with dissolve
            jump game_start

    return

label game_start:
    "You're all alone walking to the concert. Thinking about the next Vocaloid song. Hoping it's going to be awesome."
    "When suddenly..."

    scene bg studio night with dissolve
    "..." "Hey... \nStranger. Can you help me?"
    "You turn around, and suddenly. You see Hatsune Miku herself!"
    show miku wave with dissolve
    m "Hey! Can you help me? I've lost the way to the podium! And I'm going to miss the concert!"
    menu:
        "Will you help Miku?"
        "Yeah, I can!":
            $ the_player.set_choice("helped_miko",True)
            p "Yeah, I can. You're Miku right?"
            m "Yes, I am. Who want's to know?"
            $ p = renpy.input("Miku wants to know you're name!")
            $ the_player.set_name(p)
            $ p = Character(the_player.player_name)
            p "Hello, I'm [p]. I'm one of your fans!"
            m "Well, hello [p]. I'm Miku :D. But you already knew that :O."
            p "So, for the concert, you have to go right. Then 200 meters futher you see some headlights."
            p "When you're there, you can see a shirt store on your right."
            p "Keep following this way, and you end up at the concert!"
            m "Ok! Thank you :D."
            $ msg.msg("{color=#61baca}Miku {color=#808080}will remember this!")
            m "I'll see you at the concert. Here's a VIP pass for helping me!"
            $ msg.msg("{color=#808080}You've acquired a {color=#FFD700}VIP {color=#808080}pass!")
            hide miku wave with dissolve
            "..."
            scene black
            if renpy.mobile != True:
                "You walk to the concert, and find out other people know you've gotten a VIP pass. (Look at your discord)"
                python:
                    callbacks = {
                        'ready': readyCallback,
                        'disconnected': disconnectedCallback,
                        'error': errorCallback,
                    }
                    discord_rpc.initialize('564432578803662848', callbacks=callbacks, log=False)
                    start = time.time()
                    discord_rpc.update_connection()
                    discord_rpc.run_callbacks()
                    discord_rpc.update_presence(
                        **{
                            'details': 'Got a FREE VIP Pass!',
                            'state': 'Suprised :O',
                            'large_image_key': 'miku_logo',
                            'start_timestamp': start
                        }
                    )

                    discord_rpc.update_connection()
                    discord_rpc.run_callbacks()



        "No, I can't I'm in a hurry.":
            $ msg.msg("{color=#61baca}Miku {color=#808080}will remember this!")
            $ p = "..."
            $ the_player.set_choice("helped_miko",False)
            p "No, sorry I can't help you right now. I'm in a hurry."
            m "{color=#FF0000}Fine, I'll leave then."
            "Quietly, you regret this decision."
    scene bg concert night
    "Apple"
return
