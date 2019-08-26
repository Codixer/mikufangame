# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miku")
define p = Character("Miku's Fan")

image miku happy = "miku/miku happy.png"
image miku wave = "miku/miku wave.png"






label start:
    show dev eyes closed with dissolve
    "Welcome player!"
    "We know you want to start playing the game, but first. Please listen to this message."
    show mikufan at centerright with dissolve
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
        "Will you help Miku?":
            "Yeah, I can!"
                $ helped_miku = True;
                p "Yeah, I can. You're Miku right?"
                m "Yes, I am. Who want's to know?"
                $ p = renpy.input("Miku wants to know you're name!")
                $ p = p.strip()
                if p == "":
                    $ p="Miku's Fan"
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
            "No, I can't I'm in a hurry."
                "Hi"

return
