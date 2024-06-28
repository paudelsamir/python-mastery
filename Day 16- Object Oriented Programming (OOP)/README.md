# Object-Oriented Programming in Python 


## Learning Objectives
- Classes and Objects
- Inheritance
- Encapsulation
- Polymorphism
- Method Overriding
- Abstraction

## OOP Concepts and Examples

1. Classes and Objects

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says Woof!
```
2. Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"

my_cat = Cat("Whiskers")
print(my_cat.meow())  # Output: Whiskers says Meow!
```
3. Polymorphism: 
```python
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Square(5), Circle(3)]
for shape in shapes:
    print(shape.area())
```
4. Encapsulation: 
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
```

5. Method Overriding:
```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Animal(), Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())

```
6. Abstractiopn:
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

car = Car()
print(car.start_engine())  # Output: Car engine started
```