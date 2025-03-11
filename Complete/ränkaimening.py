


letters = {}



while True:
    try: 
        sentence = (input("Input your sentence: ")).lower()
        for letter in sentence: 
            if letter == " ": 
                continue
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    except KeyError:
        print("Error")
    except KeyboardInterrupt: 
        print("Exiting ....")
        break
    for x in letters:
        print(f'{str(x)} = {letters[x]}')
    letters = {}
        
    

    
    





