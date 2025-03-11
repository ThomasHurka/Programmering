import random
computerscore = 0
gameend = 0
playerscore = 0 
computeractivechoice = 0
gamerestart = ""

def gamefunction(value):
    computerchoice = [1, 2, 3]
    global computerscore 
    global playerscore  
    x = "Computer; Paper!"
    y = "Computer; Scissors!"
    z = "Computer; Rock!"
    computeractivechoice = random.choice(computerchoice)
    if value == 1:
        if computeractivechoice == 2:
            print(x)
            print("You Lose!")
            computerscore += 1
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
        elif computeractivechoice == 3:
            print(y)
            print("You Win!")
            playerscore += 1
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
        elif computeractivechoice == 1:
            print(z)
            print("Tie")
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
    elif value == 2: 
        if computeractivechoice == 1:
            print(z)
            print("You Win!")
            playerscore += 1
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
        elif computeractivechoice == 3: 
            print(y)
            print("You Lose!")
            computerscore += 1
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
        elif computeractivechoice == 2:
            print(x)
            print("Tie")
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
    elif value == 3: 
        if computeractivechoice == 1: 
            print(z)
            print("You Lose!")
            computerscore += 1 
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
        elif computeractivechoice == 2:
            print(x)
            print("You Win!")
            playerscore += 1 
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
        elif computeractivechoice == 3:
            print(y)
            print("Tie!")
            print("Computer Score:", computerscore)
            print("Player Score:", playerscore)
    else:
        print("Undefined")
        



print("Welcome to rock, paper, scissors!")
while gameend == 0: 
    if computerscore <= 2 and playerscore <= 2:
        try:
            value = int(input("Input your number! 1. Rock, 2. Paper, 3. Scissors;  "))
        except KeyboardInterrupt:
            break
        except:
            value = 99
        if value >= 1 and value <= 3:
            gamefunction(value)
        else:
            print("Invalid Number")
    elif computerscore >= 2: 
        gameend += 1 
        print("Computer Win!")
    elif playerscore >= 2: 
        gameend += 1 
        print("Player Win!")
    else: 
        print("Undefined")



        

    



