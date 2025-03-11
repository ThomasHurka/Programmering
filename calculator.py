first_number = 0
second_number =  0 





def calculator(first_number, second_number):
    print("1. Addition, 2. Substract, 3. Division, 4. Multiplication")
    print("Selection Calculation Mode; ") 
    try: 
        selection_mode = int(input("Input Selection; "))
    except ValueError:
        print("Invalid Selection")
        ifghdf


    
    








while True: 
    try: 
        first_number = int(input("Input First Number; "))
        second_number = int(input("Input Second Number; "))
        calculator(first_number, second_number)
    except KeyboardInterrupt: 
        break
    except ValueError: 
        print("Invalid Number")
    
