import random 

looping = True
hercelus = random.randint(1,100)
value = 0 
guesses = 0 
def guessingfunction(firstnumber):
    global looping
    global value  
    global guesses
    if value < 9: 
        if firstnumber < hercelus:
            value += 1 
            guesses += 1 
            print("Number Larger")
        elif firstnumber > hercelus: 
            value += 1 
            guesses += 1
            print("Number Smaller")
        elif firstnumber == hercelus:
            print("You Guessed Right!")
            print(f"Amount of Guesses; {guesses}")
            looping = False
    elif value <= 10: 
        print("You're Fucking Idiot")
        looping = False
        

while looping:
    try:   
        firstnumber = int(input("Input Guess; "))
        guessingfunction(firstnumber)
    except KeyboardInterrupt: 
        print("Cancelled")
        break
    except ValueError:
        print("Invalid Number")