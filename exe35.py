from sys import exit
def gold_room ():
    print("""\rThere is gold in this room,how much do you want to take ?
    Enter numbers only please !!!""")
    choice = int(input("> "))

    if choice < 50:
        dead("\rYou are not greedy,you win")
        exit(0)
    else:
        dead("\rYou greedy bastard !")

def dead (txt):
    print(txt,"Good job!")

def bear_room():
    """ choose either taunt bear,the bear moves and you pass,open door calls gold_room
    when you call Taunt bear again the bear kills you use sink prompt you to enter chemical to use """

    print("""
    \rThere is a bear here
    \rThe bear has some honey
    \rThe bear is infront of another door
    \rHow are you going to move the bear?
    \rEnter: \n\r"Taunt bear"\n\r"open door" \n\r"Take honey" \n\r"use the sink" """)
    bear_moved = False

    while True :

        choice = input("> ")

        if choice == "Take honey":
            dead("\r The bear looks at you then slaps your face off ,")
            exit(0)

        elif choice == "Taunt bear" and not bear_moved:
            print ("""
            \rThe bear has moved from the door,
            \rYou can go through it now.""")
            bear_moved = True
            exit(0)

        elif choice == "Taunt bear" and bear_moved:
            dead("\rThe bear gets pissed off and chews your leg out ")
            exit(0)

        elif choice == "Open door" or "Open door" and bear_moved:
            gold_room()
            exit(0)

        elif  choice == "use sink":
            chem_choice()
            exit(0)

        else :
            print("r\I got no idea what that means")
            exit(0)


def cthulhu_room():
    """ Flee fron cuthulu monster or perish """

    print(""" \r Hey here you see the great evil cthulhu,
    \rHe,it ,whateer stares at you and you go insane,
    \rDo you flee for your life or eat your head?""")
    choice = input("> ")

    if "flee" in choice :
        start()

    elif "head" in choice :
        dead("\rWell that was tasty!!")
        exit(0)

    else : cuthulu_room()

def start():
    """ This is the main function of the game it initiates other functions with regard to user input """

    print("""\rYou are in a dark room
    \rThere is a door to your right and left
    \rWhich door do you take, either right or left """)

    choice = input("> ")

    if choice == "left":
        cthulhu_room()

    elif choice ==  "right":
        bear_room()

    else :
        print("\rYou stumble around till you starve.")
        exit(0)

def chem_choice():
    """ this  function allows you to choose chemical to use for escapig """

    print(""" \r What chemical do you need to desolve cement on crack?
    \r Enter \n\r*NITRATE or nitrate
    \r*Carbonate or CARBONATE please""")

    choice = input("> ")

    if "nitrate" or "NITRATE" in choice :
        print("\rokay take the tooth paste on the sink and mix with washing powder")

    elif 'carbonate' or "CARBONATE" in choice :
        print("Learn some chemistry man !!")
        exit(0)

    else:
        print ("\rWhat the fuck you talking about?")
        exit(0)
start()
