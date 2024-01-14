print ("""you enter a room with two doors
Do you enter door #1 or do you enter door #2? """)
door = input  ("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    if bear == "1" :
        print ("The bear eats your face off, congratulations.")
    elif bear == "2":
        print ("the bear eats your kegs off ,congratulations.")
    else :
        print (f"Well doing {bear},is probably better!")
        print("The bear runs away.")
elif door == "2":
    print("You found the weed jini,what strain do you want?")
    print("""

    1. Memosa
    2.Indica
    3.Sativa
    4.Mind_Rape
    5.Cat_piss
    6.moon_pie
    7.Dragon_eyes

    Choose 1,2,3,4,5,6 or 7
    """)
    weed_strain = input("> ")

    if weed_strain == "1" or weed_strain == "2":
       print (""" You and the bear get high and everything turns out okay
    Great job !!! """)
    elif weed_strain == "3" or weed_strain == "4":
        print("you and the bear get fucked up and tear each other apart,curve baaaalll :/( :/(")
    else :
        print ("you smoked on moon_pie and Dragon_eyes till you brought about the second coming of jesus")
else :
    print (""" Demon in the room caught you and fucked your anus till you died !!!!
""")
