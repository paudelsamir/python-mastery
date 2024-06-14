

### Indentation Definition:
Indentation in Python defines code blocks.
I would like to prefer one tabs over 4 spaces.

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Sam")
```
## Functions
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