 #--------------------------------BASICS--------------------------------

# print("Hello World")              -Print

# input("What's your name")         -Input

#This is a comment                  -Comments    
# print("This is code")

# my_name = "JohnWick"              -Variables
# my_age = 12

# my_age = 12                       -The += Operator
# my_age += 4
#my_age is now 16


   



 #--------------------------------DATA TYPES--------------------------------

# my_number = 354               - INTEGERS

# my_float = 3.14159            - FLOATING POINT NUMBER

# my_string = "Hello"           -STRINGS

# "Hello" + "Samir"            -STRING CONCATINATION
# #becomes "HelloSamir"

# speech = "She said: \"Hi\""    -ESCAPING THE STRING
# print(speech)
# #prints: She said: "Hi"

# days = 365                    - F-STRING
# print(f"There are {days}
# in a year")

# n = 354                        -CONVERTING DATA TYPES
# new_n = float(n)
# print(new_n) #result 354.0

# n = 3.14159                    -CHECKING DATA TYPES
# type(n) #result float






#--------------------------------MATH--------------------------------

# 3+2 #Add          -ARITHMETIC OPERATORS
# 4-1 #Subtract
# 2*3 #Multiply
# 5/2 #Divide
# 5**2 #Exponent

# my_number = 4     -THE +=OPERATOR
# my_number += 2
# #result is 6

# 5 % 2             -THE MODULO OPERATOR
# #result is 1


  




 #--------------------------------FUNCTIONS--------------------------------

# def my_function():                    -Creating Functions
# print("Hello")
# name = input("Your name:")print("Hello")

# my_function()                          -Calling Functions
# my_function()
# #The function my_function
# #will run twice.

# def add(n1, n2):                      - Functions with Inputs
# print(n1 + n2)
# add(2, 3)

# def add(n1, n2):                       -Functions with Outputs
# return n1 + n2
# result = add(2, 3)

# n = 2                                   - Variable Scope
# def my_function():
# n = 3
# print(n)
# print(n) #Prints 2
# my_function() #Prints 3

# def divide(n1, n2):                   - Keyword Arguments
# result = n1 / n2  
# #Option 1:
# divide(10, 5)
# #Option 2:
# divide(n2=5, n1=10)






 #-------------------------CONDITIONALS-------------------------

# n = 5                          -IF
# if n > 2:
# print("Larger than 2")

# age = 18                      - ELSE
# if age > 16:
# print("Can drive")
# else:
# print("Don't drive")

# weather = "sunny"              -ELIF
# if weather == "rain":
# print("bring umbrella")
# elif weather == "sunny":
# print("bring sunglasses")
# elif weather == "snow":
# print("bring gloves")

# s = 58                         -AND
# if s < 60 and s > 50:
# print("Your grade is C")

# age = 12                        -OR
# if age < 16 or age > 200:
# print("Can't drive")

# if not 3 > 1:                  - NOT
# print("something")
# #Will not be printed.

# > Greater than                - COMPARISON OPERATORS
# < Lesser than
# >= Greater than or equal to
# <= Lesser than or equal to
# == Is equal to
# != Is not equal to





 #-------------------------LOOPS-------------------------

# n = 1                         - While Loop
# while n < 100:
# n += 1

# all_fruits = ["apple",         - For Loop
# "banana", "orange"]
# for fruit in all_fruits:
# print(fruit)

# for _ in range(100):            _- in a For Loop
# #Do something 100 times.

# scores = [34, 67, 99, 105]      - break
# for s in scores:
# if s > 100:
# print("Invalid")
# break
# print(s)

# n = 0                          - continue
# while n < 100:
# n += 1
# if n % 2 == 0:
# continue
# print(n)
# #Prints all the odd numbers

# while 5 > 1:                   - Infinite Loops
# print("I'm a survivor")






#----------------------------------------LIST METHODS---------------------------------------------

# list1 = [1, 2, 3]                   -Adding Lists Together
# list2 = [9, 8, 7]
# new_list = list1 + list2
# list1 += list2

# all_fruits = ["apple",              -Adding an Item to a List
# "banana", "orange"]
# all_fruits.append("pear")

# letters = ["a", "b", "c"]           -List Index
# letters[0]
# #Result:"a"
# letters[-1]
# #Result: "c"

# list[start:end]                     -List Slicing
# letters = ["a","b","c","d"]
# letters[1:3]
# #Result: ["b", "c"]





#-------------------------------------------BUILT IN FUNCTIONS------------------------------------

# # range(start, end, step)          - RANGE
# for i in range(6, 0, -2):
#     print(i)
# # result: 6, 4, 2
# # 0 is not included.

# import random                      - RANDOMIZATION
# # randint(start, end)
# n = random.randint(2, 5)
# #n can be 2, 3, 4 or 5.

# round(4.6)                        - ROUND
# # result 5

# abs(-4.6)                         -ABS
# # result 4.6





#--------------------------------MODULES--------------------------------

# import random                   -Importing
# n = random.randint(3, 10) 

# import random as r              -Aliasing
# n = r.randint(1, 5)

# from random import randint      -Importing from modules
# n = randint(1, 5)

# from random import *            -Importing Everything
# list = [1, 2, 3]
# choice(list)
# # More readable/understood
# #random.choice(list)







#--------------------------------CLASSES AND OBJECTS---------------------

# class MyClass:      -Creating a Python Class
# #define class

# class Car:          -Creating an Object from a Clas
# pass
# my_toyota = Car()

# class Car:          -Class Methods
# def drive(self):
# print("move")
# my_honda = Car()
# my_honda.drive()

# class Car:          -Class Variables
# colour = "black"
# car1 = Car()
# print(car1.colour) #black

# class Car:          -The __init__ method
# def __init__(self):
# print("Building car")
# my_toyota = Car()
# #You will see "building car"
# #printed.

# class Car:          -Class Properties
# def __init__(self, name):
# self.name = "Jimmy

# class Animal:       -Class Inheritance
# def breathe(self):
# print("breathing")
# class Fish(Animal):
# def breathe(self):
# super().breathe()
# print("underwater")
# nemo = Fish()
# nemo.breathe()
# #Result:
# #breathing
# #underwater
