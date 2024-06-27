import random
from art import logo

print("Welcome to the number guessing game!")
print (logo)
print("I am thinking of a number between 1 and 100.")
number = random.randint(1, 100)
# print(number)


def guess():
    
    global attempts 
    
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if attempts == 0:
        print(f"Out of attempts. The number was {number}.")
        exit()    
    if guess == number:
        print(f"You have guessed it. The number is {number}.")
        exit()
    elif guess > number:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")
    

            
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
while difficulty != 'easy' and difficulty != 'hard':
    difficulty = input("Invalid difficulty level. Please choose 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5


while not attempts == 0:
    guess()
