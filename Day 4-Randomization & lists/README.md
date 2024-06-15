
## Randomisation 
- **Randomisation**: Using the `random` module.

```python
import random

random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)
#prints the random number between 1 and 10 each time when yuo run the program
```

## List Methods
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