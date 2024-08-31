**Note:** 🚀 **I’ve learned the basics of Python before and am now revisiting them to strengthen my foundation with data.** <br><br> 
<i>This cleansheet is crafted with the help of AI tools and invaluable web resources. 
</i>


# Python Mastery: Day 1 - Cleansheets

## Concepts Covered

On the first day, I revised the following Python concepts. The syntaxes are thoroughly covered `below`:


### Basics
- **Print**: Using `print()` to display messages.
- **Input**: Using `input()` to get user input.
- **Comments**: Adding `#` for comments.
- **Variables**: Creating and using variables.
- **The `+=` Operator**: Adding to the previous value.

```python
# Example of using print()
print("Hello, world!")

# Example of getting user input
name = input("Enter your name: ")

# Example of comments
# This is a comment

# Example of variables
age = 25
name = "Alice"

# Example of using the += operator
count = 0
count += 1
print(count)  # Output: 1
```
### Data Types
- **Integers**: Whole numbers.
- **Floating Point Numbers**: Numbers with decimal places.
- **Strings**: A sequence of characters enclosed in quotes.
- **String Concatenation**: Adding strings together.
- **Escaping a String**: Using backslash `\` for special characters.
- **Converting Data Types**: Using `float()`, `int()`, `str()`.
- **Checking Data Types**: Using `type()`.
- **F-Strings**: Inserting variables into strings.

```python
# Examples of data types and operations in Python

# Integers and floating point numbers
age = 25
height = 1.75

# Strings and string operations
name = "Alice"
greeting = "Hello, " + name + "!"

# Escaping a string
message = "She said \"Hello!\""

# Converting data types
number_str = "10"
number_int = int(number_str)
number_float = float(number_str)

# Checking data types
print(type(age))      # Output: <class 'int'>
print(type(height))   # Output: <class 'float'>
print(type(name))     # Output: <class 'str'>

# F-Strings
greeting_fstring = f"Hello, {name}! You are {age} years old."
print(greeting_fstring)  # Output: Hello, Alice! You are 25 years old.
```
### Maths
- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `**`.
- **The `+=` Operator**: Convenient addition.
- **The Modulo Operator**: `%` to get the remainder of a division.

```python
# Examples of math operations in Python

# Arithmetic operators
result_addition = 10 + 5      # 15
result_subtraction = 10 - 5   # 5
result_multiplication = 10 * 5 # 50
result_division = 10 / 5       # 2.0
result_exponentiation = 2 ** 3 # 8

# The += operator
total = 0
total += 10  # total is now 10
total += 5   # total is now 15

# The modulo operator
remainder = 10 % 3  # remainder is 1

# Displaying results
print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
print("Exponentiation:", result_exponentiation)
print("Total with +=:", total)
print("Modulo:", remainder)
```
### Errors
- **Name Error**: Using an undefined variable.
- **Zero Division Error**: Dividing by zero.
- **Syntax Error**: Code that doesn't make sense to the interpreter.

```python
# Examples of common errors in Python

# Name Error
# Trying to use a variable that is not defined
# Uncomment the following line to see the error
# print(undefined_variable)

# Zero Division Error
# Dividing by zero
# Uncomment the following line to see the error
# result = 10 / 0

# Syntax Error
# Incorrect syntax that the interpreter cannot understand
# Uncomment the following line to see the error
# x = 10 y = 5
```
### Functions
- **Creating Functions**: Using `def` to define functions.
- **Calling Functions**: Executing functions by name.
- **Functions with Inputs**: Adding parameters to functions.
- **Variable Scope**: Understanding local and global variables.
- **Functions with Outputs**: Using `return` to get output from functions.
- **Keyword Arguments**: Providing arguments by name.

```python
# Examples of functions and related concepts in Python

# Creating functions
def greet():
    return "Hello, World!"

# Calling functions
greeting = greet()
print(greeting)  # Output: Hello, World!

# Functions with inputs
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(5, 3)
print("Sum:", sum_result)  # Output: Sum: 8

# Variable scope
total = 0  # Global variable

def increment():
    global total  # Access global variable
    total += 1

increment()
print("Total:", total)  # Output: Total: 1

# Functions with outputs
def square(x):
    return x ** 2

squared_value = square(4)
print("Squared value:", squared_value)  # Output: Squared value: 16

# Keyword arguments
def describe_person(name, age):
    return f"{name} is {age} years old."

description = describe_person(age=30, name="Alice")
print(description)  # Output: Alice is 30 years old.
```
### Conditionals
- **If**: Basic condition checks.
- **Else**: Specifying code to run if `if` condition is false.
- **Elif**: Additional conditions.
- **not**: Negating a condition.
- **and**: Combining conditions with AND logic.
- **or**: Combining conditions with OR logic.
- **Comparison Operators**: `>`, `<`, `>=`, `<=`, `==`, `!=`.

```python
# Examples of conditionals and comparison operators in Python

# If statement
age = 18
if age >= 18:
    print("You are an adult.")

# Else statement
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Elif statement
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")

# not operator
x = 5
if not x == 0:
    print("x is not zero")

# and operator
temperature = 25
if temperature > 0 and temperature < 30:
    print("Temperature is between 0 and 30 degrees Celsius")

# or operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Comparison operators
number = 10
if number > 5:
    print("Number is greater than 5")
if number < 20:
    print("Number is less than 20")
if number >= 10:
    print("Number is greater than or equal to 10")
if number <= 15:
    print("Number is less than or equal to 15")
if number == 10:
    print("Number is exactly 10")
if number != 5:
    print("Number is not equal to 5")
```
### Loops
- **While Loop**: Repeating actions while a condition is true.
- **For Loop**: Iterating over a sequence.
- **break**: Exiting a loop.
- **continue**: Skipping to the next iteration.
- **Infinite Loops**: Loops that never end unless interrupted.
- **`for_in` in a for loop**: Iterating a specific number of times using `range()`.

```python
# Examples of loops in Python

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
# Outputs:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Outputs:
# apple
# banana
# cherry

# break statement
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# Outputs:
# 0
# 1
# 2
# 3
# 4

# continue statement
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
# Outputs:
# 1
# 3
# 5
# 7
# 9

# Infinite loop (Interrupt with Ctrl+C to stop)
# Uncomment the following lines to run an infinite loop
# while True:
#     print("Press Ctrl+C to stop me!")

# `for_in` in a for loop
for _ in range(3):
    print("Hello, world!")
# Outputs:
# Hello, world!
# Hello, world!
# Hello, world!
```
### List Methods
- **List Index**: Accessing items by index.
- **Adding Lists Together**: Using `extend` or `+`.
- **Adding an Item to a List**: Using `append()`.
- **List Slicing**: Using `[start:end]` to get a portion of a list.

```python
# Examples of list methods in Python

# List Index
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]
print("First fruit:", first_fruit)  # Output: First fruit: apple

# Adding Lists Together
more_fruits = ["orange", "grape"]
combined_fruits = fruits + more_fruits
print("Combined fruits:", combined_fruits)  # Output: Combined fruits: ['apple', 'banana', 'cherry', 'orange', 'grape']

# Adding an Item to a List
fruits.append("pear")
print("Fruits after appending:", fruits)  # Output: Fruits after appending: ['apple', 'banana', 'cherry', 'pear']

# List Slicing
numbers = [1, 2, 3, 4, 5]
slice_of_numbers = numbers[1:4]
print("Slice of numbers:", slice_of_numbers)  # Output: Slice of numbers: [2, 3, 4]
```
### Built-in Functions
- **Round**: Rounding numbers.
- **Randomisation**: Using the `random` module.
- **Range**: Generating a range of numbers.
- **abs**: Getting the absolute value.

```python
# Examples of built-in functions in Python

# Round
num1 = 3.14159
rounded_num = round(num1, 2)
print("Rounded number:", rounded_num)  # Output: Rounded number: 3.14

# Randomisation (using the `random` module)
import random

random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)

# Range
numbers = list(range(1, 6))
print("Range of numbers:", numbers)  # Output: Range of numbers: [1, 2, 3, 4, 5]

# abs
absolute_value = abs(-10)
print("Absolute value:", absolute_value)  # Output: Absolute value: 10
```
### Modules
- **Aliasing**: Using `as` to rename modules.
- **Importing**: Importing pre-installed and third-party modules.
- **Importing Everything**: Using `*` to import all functions from a module.
- **Importing Specific Functions**: Importing specific functions from a module.

```python
# Examples of module usage in Python

# Aliasing
import math as m
print("Square root of 16:", m.sqrt(16))  # Output: Square root of 16: 4.0

# Importing
import random
print("Random number between 1 and 10:", random.randint(1, 10))

# Importing Everything
from math import *  # Avoid using `*` in actual code for clarity
print("Value of pi:", pi)  # Output: Value of pi: 3.141592653589793

# Importing Specific Functions
from random import randint
print("Random number between 1 and 100:", randint(1, 100))
```
### Classes and Objects
- **Creating Python Class**: You create a class using the `class` keyword.
- **Creating an Object from a Class**: You can create a new instance of an object by using the `class name()` syntax.
- **Class Methods**: Functions that belong to a class are known as methods.
- **Class Variables**: Variables defined in a class are accessible to all objects created from the class.
- **The `__init__` method**: This method is called every time a new object is created from the class (constructor).
- **Class Properties**: Variables initialized in the `__init__` method are accessible to all objects created from the class.
- **Class Inheritance**: When creating a new class, you can inherit the methods and properties of another class.

```python
# Examples of classes and objects in Python

# Creating a Python class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object from a class
car1 = Car("Toyota", "Corolla")
car1.display_info()  # Output: Car: Toyota Corolla

# Class methods
class Circle:
    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return self.pi * self.radius ** 2

circle1 = Circle(5)
print("Area of circle:", circle1.calculate_area())  # Output: Area of circle: 78.5

# Class variables
class Dog:
    species = "Canine"
    
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
print("Species of dog:", dog1.species)  # Output: Species of dog: Canine

# The __init__ method and class properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Alice", 30)
person1.display_info()  # Output: Name: Alice, Age: 30

# Class inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

student1 = Student("Bob", 25, "S12345")
student1.display_info()
# Output:
# Name: Bob, Age: 25
# Student ID: S12345
```

