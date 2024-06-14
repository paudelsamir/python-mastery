## Loops
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