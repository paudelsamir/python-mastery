#BASICS
# print("Hello World")

# input("What's your name")

#This is a comment
# print("This is code")


# my_name = "Angela"
# my_age = 12

# my_age = 12
# my_age += 4
#my_age is now 16





#DATA TYPES
# my_number = 354      - INTEGERS

# my_float = 3.14159       - FLOATING POINT NUMBER

# my_string = "Hello"       -STRINGS

# "Hello" + "Angela"        -STRING CONCATINATION
# #becomes "HelloAngela"

# speech = "She said: \"Hi\""       -ESCAPING THE STRING
# print(speech)
# #prints: She said: "Hi"

# days = 365               - F-STRING
# print(f"There are {days}
# in a year")

# n = 354                   -CONVERTING DATA TYPES
# new_n = float(n)
# print(new_n) #result 354.0

# n = 3.14159           -CHECKING DATA TYPES
# type(n) #result float




#MATH



# 3+2 #Add          -ARITHMETIC OPERATORS
# 4-1 #Subtract
# 2*3 #Multiply
# 5/2 #Divide
# 5**2 #Exponent


# my_number = 4         -THE +=OPERATOR
# my_number += 2
# #result is 6

# 5 % 2             -THE MODULO OPERATOR
# #result is 1







#FUNCTIONS
# def my_function():      -Creating Functions
# print("Hello")
# name = input("Your name:")print("Hello")




# my_function()           -Calling Functions
# my_function()
# #The function my_function
# #will run twice.



# def add(n1, n2):        Functions with Inputs
# print(n1 + n2)
# add(2, 3)



# def add(n1, n2):            Functions with Outputs
# return n1 + n2
# result = add(2, 3)



# n = 2                   Variable Scope
# def my_function():
# n = 3
# print(n)
# print(n) #Prints 2
# my_function() #Prints 3




# def divide(n1, n2):         Keyword Arguments
# result = n1 / n2
# #Option 1:
# divide(10, 5)
# #Option 2:
# divide(n2=5, n1=10)







# #CONDITIONALS

# n = 5                   IF
# if n > 2:
# print("Larger than 2")



# age = 18                ELSE
# if age > 16:
# print("Can drive")
# else:
# print("Don't drive")


# weather = "sunny"           ELIF
# if weather == "rain":
# print("bring umbrella")
# elif weather == "sunny":
# print("bring sunglasses")
# elif weather == "snow":
# print("bring gloves")



# s = 58                      AND
# if s < 60 and s > 50:
# print("Your grade is C")




# age = 12                    OR
# if age < 16 or age > 200:
# print("Can't drive")




# if not 3 > 1:               NOT
# print("something")
# #Will not be printed.



# > Greater than          COMPARISON OPERATORS
# < Lesser than
# >= Greater than or equal to
# <= Lesser than or equal to
# == Is equal to
# != Is not equal to