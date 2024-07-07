# Python File Handling Basics


## Table of Contents
1. [Opening and Closing Files](#opening-and-closing-files)
2. [Using 'with' Statement](#using-with-statement)
3. [Reading Files](#reading-files)
4. [Writing to Files](#writing-to-files)
5. [Appending to Files](#appending-to-files)
6. [Checking if a File Exists](#checking-if-a-file-exists)

## Opening and Closing Files

```python
# Open a file for writing
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

# Open a file for reading
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

## Using 'with' Statement

The 'with' statement is recommended as it automatically closes the file after you're done:

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## Reading Files

```python
# Read entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

## Writing to Files

```python
# Write a single string
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Write multiple lines
lines = ["Line 1", "Line 2", "Line 3"]
with open("example.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
```

## Appending to Files

```python
with open("example.txt", "a") as file:
    file.write("\nThis is a new line")
```

## Checking if a File Exists

```python
import os

if os.path.exists("example.txt"):
    print("The file exists")
else:
    print("The file does not exist")
```

