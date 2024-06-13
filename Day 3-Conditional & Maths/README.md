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