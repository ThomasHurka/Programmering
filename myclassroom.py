








class Student:
    def __init__(self, fname : str, lname : str, year : int, grades : list[int]):
        self.fname = fname
        self.lname = lname
        self.year = year
        self.grades = grades
    def changeVariables(self, newfname : str, newlname : str, newyear : int, newgrades : list[int]):
        self.fname = newfname
        self.lname = newlname
        self.year = newyear
        self.grades.append(newgrades)
    def printInformation(self):
        print(F'Their name is {self.fname} {self.lname}, they came to this school in {self.year}, These are their grades: {self.grades}')
        averagegrades = float(sum(self.grades) / len(self.grades))
        print(f'Their grade average is {averagegrades}')

class Classrom: 
    def __init__(self, name : str, students : list):
        self.name = name 
        self.students = students 
        print(students)
        
    
s1 = Classrom()
p1 = Student("Kanna", "Kamui", 2017, [5, 5, 5, 5, 5])
p2 = Student("Elias", "Sjöling Njord", 2002, [5,5,5,5,5,5,5,5,4])


p1.printInformation()
p2.printInformation()









# fnamechange = str(input("Input your first name: "))
# lnamechange = str(input("Input your last name: "))
# yearchange = int(input("Input the year you started: "))
# gradechange = list(map(int(input(" Input your grades: ").split())))




    








