"""item = "potato chips"
price = 35.45
quantity = 100
isFood = True
"""
#print(type())

"""numberStr = "10.40"
number = 10.25
numberStr = float(numberStr)

total = numberStr + number

print (type(numberStr))
print(total)"""

"""name = "This is my name"
name = bool(name)

print(type(name))"""

#print("enter your first name:")
"""Firstname = input("enter your first name: ") 
print(f"Hi {Firstname}!")"""

"""numberOne = input("enter a value of num one: ")
numberTwo = input("enter a value of num two: ")"""

"""numberOne = int(numberOne)
numberTwo = int(numberTwo)
sum = numberOne + numberTwo
print(f"the sum of two numbers is {sum}")"""

#Exercise 1
"""W = int(input("enter your width: "))
L = int(input("enter your length: "))

A = W * L

print(f"A = {A}")"""

#Exercise 2
"""print(input("what item would you like to buy?"))

price = float(input("what's the price? "))
quantity = int(input("how many would you like to buy? "))

total = price * quantity

print(f"Your total would be {total}")"""

"""age = int(input("Enter ur age: "))

if age <= 5:
    print("why r u on the puter little bro")
elif age >= 13 and age <= 19:
    print("teenage dirtbag?")
else:
    print("what is up unc")"""
    
#example wan

"""number = 7

result = "postive" if number > 0 else "negative"

print(f"the result is {result}")"""

#example two

"""min = int(input("enter a minimum value: "))
max = int(input("enter a maximum value: "))

result = min if min < max else max 
print(f"the result is {result}")"""

#example 3

"""text = input("enter a text: ")"""

"""print(f"the length of the text is {len(text)}")"""

"""result = text.find("p")
print(result)"""
"""resultOne = text.capitalize()
resultTwo = resultOne.upper()
resultThree = resultTwo.lower()
print(f"Capitalize: {resultOne}, Upper: {resultTwo}, Lower: {resultThree}")"""
"""result = text.isdigit()"""
#result = text.isalpha()
"""result = text.count("T")
print(result)"""

#exercise wan

"""username = input("please enter username: ")

if " " in username:
    print("Error: Username must not contain spaces.")
elif len(username) > 12:
    print("Your username must not go beyond 12 characters.")
elif not username.isalpha():
    print("your user must not contain a digit.")
else:
    print(f"welcome {username}!!")"""
    
"""credit_card = "1267-2546-7674-9672"
last_four = credit_card[-4:]
print("last four digits:", last_four)

reversed_card = credit_card[::-1]
print("reversed:", reversed_card)"""
    
#example: loops

#WHILE

"""username = input("enter ur username: ")

while username == "":
    print("u didnt enter ur username")
    username = input("enter ur username: ")
    
print(f"welcome {username}!")
"""

"""number = int(input("enter a numbah: "))

while number < 1 or number > 20:
    if number < 1:
        print("the number u entered is less than 1 :p")
        number = int(input("enter a numbah: "))
    elif number > 20:
        print("ur number is bigger than 20 man")
        number = int(input("enter a numbah: "))
    
print(f"number is {number}")"""

"""favfood = input("enter ur fav food (enter q to quit): ")

while not favfood == "q":
    print(f"ur favfood is {favfood}")
    favfood = favfood = input("enter another fav food (enter q to quit): ")
    
print("thank u for telling me ur fav food")
"""

"""for x in range(1, 10):
    if x == 6:
        print(x)
        break
    else:
     print(x, end=",")"""
     
"""colors = ["red","blue","yellow"]
colors.append("green")
colors.append("periwinkle")

print(colors[::-1])

#list to while

index = 0

while index < len(colors):
    print(f"colors: {colors[index]}")
    index += 1
    
print("thats all da colors")

#list to loop

for x in range(2, len(colors)):
    print(f"colors: {colors[x]}")"""
    
#example: fanction

"""def addition(numberwan, numbertwo):
    sum = numberwan + numbertwo
    print(f"the sum of two numbers is {sum}")
    
addition(12, 55)
"""

"""def addition(Name, Age, Country):
    print(f"Their name is {Name}, their Age is {Age}, and their Country is {Country}")

addition("Raymond", 34, "USA")"""
    
#example: class

class Student:
    
    total_student = 0
    total_GPA = 0
    
    def __init__(self, name, course, GPA):
        self.name = name
        self.course = course
        self.GPA = GPA
        Student.total_student += 1
        Student.total_GPA += GPA
        
        
    def get_info(self):
        print(f"my name is {self.name}, my course is {self.course}")
        
    @staticmethod
    def isValid_course(course):
        valid_course = ["BSCS", "BMMA", "BSEMC"]
        for x in valid_course:
           if x == course:
               print("this is a valid course")
               
    @classmethod
    def get_average_GPA(cls):
        ave = cls.total_GPA / cls.total_student
        print(f"the average gpa of all is {ave}")
               
               

studentOne = Student("Fred", "BMMA", 87.43)
studentTwo = Student("Gerry", "BSCS", 92.11)
studentThree = Student("Larry", "BSEMC", 78.59)

print(f"Student one name: {studentOne.name}, Course {studentOne.course}")
print(f"Student two name: {studentTwo.name}, Course {studentTwo.course}")
print(f"Student three name: {studentThree.name}, Course {studentThree.course}")

#Student.isValid_course(studentTwo.course)
Student.get_average_GPA()

#studentOne.get_info()
