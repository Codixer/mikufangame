# The script of the game goes in this file.
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

        

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miku")
define p = Character("Miku's Fan")

image miku happy = "miku/miku happy.png"
image miku wave = "miku/miku wave.png"






label start:
    $ the_player = Player()
    show dev eyes closed with dissolve
    "Welcome player!"
    "We know you want to start playing the game, but first. Please listen to this message."
    show mikufan at center with dissolve
    "You may have downloaded the game from the Mikufan discord!"
    hide dev eyes closed with dissolve
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
        "No, I can't I'm in a hurry.":
            "Hi"
    
    "[the_player.player_name] helped Miko?"

    if the_player.get_choice("helped_miko"):
        "Yes [the_player.player_name] helped Miko"
        $ the_player.set_choice("tile","Miko Supporter")
    else:
        "No [the_player.player_name] helped Miko"
        $ the_player.set_choice("tile","Do not want to support Miko")

    $ title = the_player.get_choice("tile")

    "So your current Tile is [title]"

return
