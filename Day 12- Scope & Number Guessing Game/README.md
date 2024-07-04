# Python Scopes

## Overview
In Python, a scope refers to the region of code where a variable is accessible. Understanding scopes is crucial for proper variable management and avoiding naming conflicts.

## Types of Scopes

### 1. Local Scope
- Variables defined within a function
- Accessible only inside that function

### 2. Enclosing Scope
- For nested functions
- Variables in the outer (enclosing) function

### 3. Global Scope
- Variables defined at the top level of a module
- Accessible throughout the module

### 4. Built-in Scope
- Names preassigned in Python (like `print`, `len`)
- Always accessible

## Key Points
- Python searches for variables in LEGB order: Local, Enclosing, Global, Built-in
- Use `global` keyword to modify global variables within a function
- Use `nonlocal` keyword in nested functions to modify variables from the enclosing scope

## Example
```python
x = 10  # Global scope

def outer():
    y = 20  # Enclosing scope
    def inner():
        z = 30  # Local scope
        print(x, y, z)
    inner()

outer()