import psphelper
title = " Battle of the Sexes (B.O.T.S) "
fillchar = "="
print(title.center(50, fillchar))

names = ["Player 1", "Player 2"]
subjects = ["1S", "2S", "3S", "4S","Trio","Quartet","Band","Doremi","Orchestra"]
marksList = [ 
    [None, None, None, None, None, None, None, None, None,], # Player 1's marks
    [None, None, None, None, None, None, None, None, None,], # Player 2's marks
]
title = "Scoreboard"
psphelper.ShowTableByList(title, names, subjects, marksList)

totalscoreP1 = 0
totalscoreP2 = 0

print(f"\nPlayer 1: {totalscoreP1}")
print(f"Player 2: {totalscoreP2}")

#Dice Roll starts here
dicerolls = []
counter = 0
roundroll = 0

input("\nPress ENTER to roll dice.")

import random

while counter != 5 :

    dicerolls.append(random.randint(1,4))
    counter += 1

roundroll += 1

print (f"\nRoll #{roundroll} : {dicerolls}\n")

names_CS = []
subjects = ["1S", "2S", "3S", "4S","Trio","Quartet","Band","Doremi","Orchestra"]
marksList = [ 
    [None, None, None, None, None, None, None, None, None,], # Alice's marks
]
title_CS = "Category Score"
psphelper.ShowTableByList(title_CS, names_CS, subjects, marksList)

print("\nInput Options:")
print("SAVE             :- Accept these dice.")
print("ROLL             :- Re-roll ALL dice.")
print("ROLL d1 ... dn   :- Re-roll specified dice only.")

P1input = str(input("Input > ")).lower()
P1input = P1input.strip("")

if P1input == "save":
        print("SAVED!")

elif P1input == "":

    counter = 0
    dicerolls = []

    while counter != 5 :

        dicerolls.append(random.randint(1,4))
        counter += 1

    print (f"\nRoll #1 : {dicerolls}\n")

else:
    P1input = P1input.strip("")
    P1input = P1input.split()
    pos = sorted(int(x)for x in P1input)

    counter = 0
    dicerollsnew = []

    while counter != len(pos) :

        dicerollsnew.append(random.randint(1,4))
        counter += 1

        for x,y in zip(pos,dicerollsnew):
            dicerolls[x] = y
    
    print (f"\nRoll #1 : {dicerolls}\n")
