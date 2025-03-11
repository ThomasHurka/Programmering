

def numbersum(firstnumber, secondnumber):
    theforce1 = sum(int(x) for x in str(firstnumber)) #Pluses together all the numbers in the variable, usage of string is because motherfucker didnt wanna do it in int
    theforce2 = sum(int(x) for x in str(secondnumber))
    #Prints out the two numbers then prints out an arrow as well and then the comparison between them aswell
    #the f-string is to format the comparisons and calculations and print them out in a understandable text
    print(f"{theforce1} == {theforce2} -> {theforce1 == theforce2}")
    #I've seen this raw strength only once before. It didn't scare me enough then. It does now.

def run():
    #Loops the code so you can feed it bunch of shit
    while True:
        try:
            #Inputs first numbers
            firstnumber = int(input("First number: "))
            secondnumber = int(input("Second number: "))
            numbersum(firstnumber, secondnumber)
            #Do. Or do not. There is no try
        except KeyboardInterrupt:
            #Without it, you couldn't escape hyperspace
            print("Exiting The Starbase")
            break
        except ValueError:
            #If number is not recognized, it warns the user
            print("Invalid Number")
            #Be mindful of your thoughts Anakin. They'll betray you.
            
#Runs the function, I’m just a simple man trying to make my way in the universe
run()