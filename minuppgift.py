import random 
specialCharacters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '~', '`', '{', '}', '[', ']',
     '|', ';', ':', '\\', '"', '<', '>', ',', '.',
    '/', '?']
numberSelection = [
    '0','1','2','3','4','5','6','7','8','9'
]

bigLetters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
smallLetters = []

passwordRandomizer = []

passwordString = []
def characterSelector():
    for i in range(lengthConfirm):
        selection = random.choice(passwordRandomizer[random.randrange(0, len(passwordRandomizer))])
        passwordString.append(selection)
        



while True:
    try: 
        lengthConfirm = int(input("What is the passwords length?; "))
        biglettersConfirm = input("Should some of the letters be big? Y/N; ").lower()
        numbersConfirm = input("Should there be numbers? Y/N; ").lower()
        specialConfirm = input("Should there be special characters? Y/N; ").lower()
        for x in bigLetters: 
            smallLetters.append(x.lower())
        passwordRandomizer.append(smallLetters)
        if biglettersConfirm == "y":
            passwordRandomizer.append(bigLetters)
        if numbersConfirm == "y": 
            passwordRandomizer.append(numberSelection)
        if specialConfirm == "y": 
            passwordRandomizer.append(specialCharacters)
        characterSelector()
        print(passwordString)
        password = "".join(passwordString)
        print(password)
        passwordString = []
        password = ""
        passwordRandomizer = []
    except lengthConfirm < 0:
        print("Loser")
    except ValueError:
        print("Value Error")
    except KeyboardInterrupt:
        print("Exiting The Starbase")
        break
    except KeyError:
        print("Key Error")



