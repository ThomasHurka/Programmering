import random


list_of_lists = ["Unsure", "Shake Again","Kys"], ["No","No Chance","Never"], ["Yes","Likely","Very likely","Most Likely"]


while True:
    try:
        user_question = input("Input your question:  ")
        print(random.choice(list_of_lists[random.randrange(0, len(list_of_lists))]))
    except KeyboardInterrupt: 
        break