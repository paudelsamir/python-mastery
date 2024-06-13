# Manipulating Data Types in Python

## Data Types

Python provides several built-in data types. Some of the most common ones include:

- **Integers (`int`)**: Whole numbers, e.g., `5`, `-3`
- **Floating Point Numbers (`float`)**: Decimal numbers, e.g., `3.14`, `-0.001`
- **Strings (`str`)**: Text data, e.g., `"hello"`, `'Python'`
- **Booleans (`bool`)**: Logical values, `True` or `False`

## Manipulating Data Types

Python allows various operations to manipulate these data types:

### Strings
- **Concatenation**: Combine strings using `+`
  ```python
  "Hello, " + "world!"  # "Hello, world!"
- **F-Strings:**
You can insert a variable into a string
using f-strings.
The syntax is simple, just insert the variable
in-between a set of curly braces {}.
    ```python
    days = 365
    print(f"There are {days} in a year")
- **Converting Data Types:**
You can convert a variable from 1 data
type to another.
    ```python 
    #Converting to float:
    float()
    #Converting to int:
    int()
    #Converting to string:
    str()
- **Checking Data Types:**
You can use the type() function
to check what is the data type of a
particular variable.
    ```python
    n = 3.14159
    type(n) #result float
