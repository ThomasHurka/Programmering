import datetime


looping = True

def calculation(firstdate : datetime ,seconddate : datetime):
    userselection : datetime = seconddate - firstdate 
    daydiff = userselection.days
    meterdiff = endingmetersetting - startingmetersetting 
        
    calculationöre = ((daydiff * dailycost) + (meterdiff * costperkilowatt)) * 1.25
    print(calculationöre)


while looping:
    try: 
        year1 = int(input("1: Input Year; "))
        month1 = int(input("1: Input Month; "))
        day1 = int(input("1: Input Day; "))

        year2 = int(input("2: Input Year; "))
        month2 = int(input("2: Input Month; "))
        day2 = int(input("2: Input Day; "))
        
        startingmetersetting = int(input("Starting Meter Setting; "))
        endingmetersetting = int(input("Ending Meter Setting; "))

        costperkilowatt = int(input("Input Öre/Kwh Cost; "))

        dailycost = int(input("Daily Cost In Öre; "))
        firstdate = datetime.datetime(year1, month1, day1)
        seconddate = datetime.datetime(year2, month2, day2)
         

        calculation(firstdate, seconddate)
        
        
        
        print("Calculation Complete")
        looping = False
    except ValueError: 
        print("Invalid Number")
    except KeyboardInterrupt: 
        break 
    

