### Basic Inheritance:
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Output: Woof!
```
### Inheriting and extending methods:

``` python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car = Car("Toyota", "Corolla")
print(car.brand, car.model)  # Output: Toyota Corolla
```

### Multiple Inheritance
``` python
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()   # Output: Flying
duck.swim()  # Output: Swimming
```

### Method Resolution Order
``` python
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        print("B")

class C(A):
    def greet(self):
        print("C")

class D(B, C):
    pass

d = D()
d.greet()  # Output: B (follows MRO: D -> B -> C -> A)
```

## Slicing 
``` python
# Create a sample list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original list:", my_list)

# Basic slicing
print("Basic slicing:")
print("my_list[2:6] =", my_list[2:6])  # Elements from index 2 to 5

# Omitting slice parameters
print("\nOmitting slice parameters:")
print("my_list[:4] =", my_list[:4])    # First 4 elements
print("my_list[6:] =", my_list[6:])    # Elements from index 6 to the end
print("my_list[:] =", my_list[:])      # Entire list

# Negative indexing
print("\nNegative indexing:")
print("my_list[-3:] =", my_list[-3:])  # Last 3 elements
print("my_list[:-2] =", my_list[:-2])  # All but last 2 elements

# Using step
print("\nUsing step:")
print("my_list[::2] =", my_list[::2])   # Every 2nd element
print("my_list[::-1] =", my_list[::-1]) # Reverse the list

# Slicing with negative step
print("\nSlicing with negative step:")
print("my_list[8:3:-1] =", my_list[8:3:-1])  # From index 8 to 4, backwards

# String slicing
text = "Python Slicing"
print("\nString slicing:")
print("text[7:] =", text[7:])     # "Slicing"
print("text[:6] =", text[:6])     # "Python"
print("text[::2] =", text[::2])   # "Pto lcn"

# Modifying list with slicing
print("\nModifying list with slicing:")
my_list[2:5] = [20, 30, 40]
print("After my_list[2:5] = [20, 30, 40]:", my_list)

# Deleting with slices
print("\nDeleting with slices:")
del my_list[1:4]
print("After del my_list[1:4]:", my_list)
```