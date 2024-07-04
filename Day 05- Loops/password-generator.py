# Basically We need to create a Strong password by taking input from user to choose the length and type of password:
# We can use imprort strings for stirngs and ascii characters
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

""" ease LEVEL - First Way """
# password = ""
# print("Welcome to sPassword Generator: ")
# pass_letters = int(input("How many letters do you want in your password? "))
# for letter in range(1, pass_letters+1):
#    password +=(letters[random.randint(0, len(letters))])  #random.choice(letters) ----> We can also do that

# pass_numbers = int(input("How many numbers do you like? "))
# for number in range(1, pass_numbers+1):
#    password +=(numbers[random.randint(0, len(numbers))])
 
# pass_symbols = int(input("How many symbols do you like? "))
# for symbol in range(1, pass_symbols+1):
#     password +=(symbols[random.randint(0, len(symbols))])

# print(password)


# print(let+num+sym)

# print(letters[random_letters]+ numbers[random_numbers]+symbols[random_symbols])

# print((letters[random_letters])*pass_letters)
# print((symbols[random_symbols])*pass_symbols)
# print((numbers[random_numbers])*pass_numbers)

"""Ease LEVEL- Second Way """
# print("Welcome to sPassword Generator: ")
# pass_letters = int(input("How many letters do you want in your password? "))
# pass_numbers = int(input("How many numbers do you like? "))
# pass_symbols = int(input("How many symbols do you like? "))


# password = ""
# for char in range(1, pass_letters+1):
#     password += random.choice(letters)
#     # print(password)
# for char in range(1, pass_numbers+1):
#     password += random.choice(numbers)

# for char in range(1, pass_symbols+1):
#     password += random.choice(symbols)

# print(password)


"""Hard LEVEL  (This will generate the shuffled password in order of your choice)""" 

print("Welcome to sPassword Generator: ")
pass_letters = int(input("How many letters do you want in your password? "))
pass_numbers = int(input("How many numbers do you like? "))
pass_symbols = int(input("How many symbols do you like? "))


password_list = []  #Creating an empty list
for char in range(1, pass_letters+1):
    password_list += random.choice(letters)
    # print(password)
for char in range(1, pass_numbers+1):
    password_list += random.choice(numbers)

for char in range(1, pass_symbols+1):
    password_list += random.choice(symbols)

print(password_list)
password = ""
random.shuffle(password_list)  # easier way  to shuffle the list This
print(password_list) 

for char in password_list:
    password = password +char

print(f"You can use the password : {password}")


    

