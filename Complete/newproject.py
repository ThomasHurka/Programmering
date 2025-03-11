def addition(x, y):
    return(x + y)

def substraction(x, y):
    return(x - y)

def multiplication(x, y): 
    return(x * y)

def division(x, y):
    return(x / y)

print("Welcome To Calculating Math Problems!")
user_input1 = int(input("Add First Number: "))
user_input2 = int(input("Add Second Number: "))
user_mode_selection = int(input("1. Addition, 2. Substraction, 3. Multiplication, 4. Division:  "))


if user_mode_selection == 1: 
    print(addition(user_input1, user_input2))
elif user_mode_selection == 2: 
    print(substraction(user_input1, user_input2))
elif user_mode_selection == 3: 
    print(multiplication(user_input1,user_input2))
elif user_mode_selection == 4: 
    print(division(user_input1,user_input2))
elif user_mode_selection < 1: 
    print("fuckoff")
elif user_mode_selection > 4: 
    print("fuck off")



    