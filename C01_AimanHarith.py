####################################################
# Program: C01_AimanHarith.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: C01
# Year: 2019/20 Trimester 1
# Name: Aiman Harith | Anas Azul
# ID: 1181103250 | 1181102772
# Email: aharith.edn@gmail.com | anashot.as@gmail.com
# Phone: 019 233 3601 | 012 636 7632
####################################################

print ("Aiman Harith")
print("1181103250")

#Imports
import psphelper
from random import randrange
import random

def normalDice():
    return [randrange(1, 5) for i in range(5)]

#Category Scores
def ones(dicelistcheck):
    return dicelistcheck.count(1)*1

def twos(dicelistcheck):
    return dicelistcheck.count(2)*2

def threes(dicelistcheck):
    return dicelistcheck.count(3)*3

def fours(dicelistcheck):
    return dicelistcheck.count(4)*4

def trio(dicelistcheck):
        if dicelistcheck.count(1) >= 3:
            return sum(dicelistcheck)
        elif dicelistcheck.count(2) >= 3:
            return sum(dicelistcheck)
        elif dicelistcheck.count(3) >= 3:
            return sum(dicelistcheck)
        elif dicelistcheck.count(4) >= 3:
            return sum(dicelistcheck)
        else:
            return 0

def quartet(dicelistcheck):
        if dicelistcheck.count(1) >= 4:
            return sum(dicelistcheck)
        elif dicelistcheck.count(2) >= 4:
            return sum(dicelistcheck)
        elif dicelistcheck.count(3) >= 4:
            return sum(dicelistcheck)
        elif dicelistcheck.count(4) >= 4:
            return sum(dicelistcheck)
        else:
            return 0

def doremi(dicelistcheck):
    dicelistcheck = list(dict.fromkeys(dicelistcheck))
    if sorted(dicelistcheck) != [1,2,3,4]:
        return 0
    else:
        return 20

def band(dicelistcheck):
    ref = list(dict.fromkeys(dicelistcheck))
    if len(ref) == 2:
        for x in ref:
            if dicelistcheck.count(x) in range(2,4):
                return 30
            else:
                return 0
    else:
        return 0

def orchestra(dicelistcheck):
    if dicelistcheck.count(1) == 5:
        return 40
    elif dicelistcheck.count(2) == 5:
        return 40
    elif dicelistcheck.count(3) == 5:
        return 40
    elif dicelistcheck.count(4) == 5:
        return 40
    else:
        return 0


currentDice = []
p1Score = 0
p2Score = 0
playerTotal = [p1Score,p2Score]
scoreList = [ 
    [None, None, None, None, None, None, None, None, None,], # Player 1's marks
    [None, None, None, None, None, None, None, None, None,], # Player 2's marks
]
scoreCheck = [
    [ones(currentDice), twos(currentDice), threes(currentDice), fours(currentDice), trio(currentDice), quartet(currentDice), band(currentDice), doremi(currentDice), orchestra(currentDice),]
]
names = ["Player 1", "Player 2"]
scoreCategory = ["1S", "2S", "3S", "4S","Trio","Quartet","Band","Doremi","Orchestra"]
position = []

roundNum = 0
while roundNum < 19:

    print("Battle of the Sexes (B.O.T.S)".center(100, "="))
    psphelper.ShowTableByList("Scoreboard", names, scoreCategory, scoreList)
    print(f"Player 1: {playerTotal[0]}")
    print(f"Player 2: {playerTotal[1]}" + "\n")

    if roundNum == 18:
        break

    playerTurn = roundNum%2
    print(f"Player {playerTurn + 1}")
    print("========")
    input("Press ENTER to roll dice.\n")

    i = 1
    while i < 4:
        if position == []:
            currentDice = normalDice()

        else:
            for x in position:
                currentDice[x-1] = random.randint(1,4)
                position = []

        scoreCheck = [[ones(currentDice), twos(currentDice), threes(currentDice), fours(currentDice), trio(currentDice), quartet(currentDice), band(currentDice), doremi(currentDice), orchestra(currentDice)]]
        print(f"Roll #{i} : {currentDice}\n")

        psphelper.ShowTableByList("Scoreboard", [], scoreCategory, scoreCheck)
        if i == 3:
            break
        print("\nInput Options:")
        print("SAVE             :- Accept these dice.")
        print("ROLL             :- Re-roll ALL dice.")
        print("ROLL d1 ... dn   :- Re-roll specified dice only.")

        while True:
            playerInput = input("Input > ")
            print(" ")
            playerInput = playerInput.lower()
            print(playerInput)
            
            if "cheat" in playerInput:
                position = playerInput.split(" ")
                position.remove('cheat')
                position = list(map(int,position))
                if len(position) == 5:
                    scoreCheck = [[ones(position), twos(position), threes(position), fours(position), trio(position), quartet(position), band(position), doremi(position), orchestra(position)]]
                    psphelper.ShowTableByList("Scoreboard", [], scoreCategory, scoreCheck)
                    i = 4
                    break

            if playerInput == "save":
                i = 4
                break

            elif "roll" in playerInput:
                position = playerInput.split(" ")
                position.remove('roll')
                position = list(map(int,position))
                if any(x < 1 or x > 5 for x in position):
                    print("ERROR : Invalid input.")
                    continue
                else:
                    i += 1
                    break

            else:
                print("ERROR : Invalid input.")
                continue

            break
        
    while True:

        inputCategory = input("\nEnter your desired category: ")
        inputCategory = inputCategory.lower()
        if inputCategory == "1s":
        
            if scoreList[playerTurn][0] == None:
                scoreList[playerTurn][0] = (ones(currentDice))
                playerTotal[playerTurn] += (ones(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue    
               
        elif inputCategory == "2s":

            if scoreList[playerTurn][1] == None:
                scoreList[playerTurn][1] = (twos(currentDice))
                playerTotal[playerTurn] += (twos(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue       
                
        elif inputCategory == "3s":

            if scoreList[playerTurn][2] == None:
                scoreList[playerTurn][2] = (threes(currentDice))
                playerTotal[playerTurn] += (threes(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue   
                
        elif inputCategory == "4s":
    
            if scoreList[playerTurn][3] == None:
                scoreList[playerTurn][3] = (fours(currentDice))
                playerTotal[playerTurn] += (fours(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue    
                
        elif inputCategory == "trio":

            if scoreList[playerTurn][4] == None:    
                scoreList[playerTurn][4] = (trio(currentDice))
                playerTotal[playerTurn] += (trio(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue     
                
        elif inputCategory == "quartet":

            if scoreList[playerTurn][5] == None:    
                scoreList[playerTurn][5] = (quartet(currentDice))
                playerTotal[playerTurn] += (quartet(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue   
                
        elif inputCategory == "band":

            if scoreList[playerTurn][6] == None:    
                scoreList[playerTurn][6] = (band(currentDice))
                playerTotal[playerTurn] += (band(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue     
                
        elif inputCategory == "doremi":

            if scoreList[playerTurn][7] == None:    
                scoreList[playerTurn][7] = (doremi(currentDice))
                playerTotal[playerTurn] += (doremi(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue    
                
        elif inputCategory == "orchestra":

            if scoreList[playerTurn][8] == None:    
                scoreList[playerTurn][8] = (orchestra(currentDice))
                playerTotal[playerTurn] += (orchestra(currentDice))
            
            else:    
                print(f"ERROR: Category '{inputCategory}' has been used.")
                continue 
                
        else: 
            print(f"ERROR: Category '{inputCategory}' does not exist.")
            continue  

        break
    roundNum += 1
    psphelper.ClearScreen()  

if playerTotal[0] > playerTotal[1]:
    print(f"Player 1 is the winner with a score of {playerTotal[0]}!")
elif playerTotal[0] > playerTotal[1]:
    print(f"Player 2 is the winner with a score of {playerTotal[1]}!")
elif playerTotal[0] == playerTotal[1]:
    print("It's a tie!")