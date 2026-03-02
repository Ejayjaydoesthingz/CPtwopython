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
    
credit_card = "1267-2546-7674-9672"
last_four = credit_card[-4:]
print("last four digits:", last_four)

reversed_card = credit_card[::-1]
print("reversed:", reversed_card)
    

