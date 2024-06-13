height = int(input("What's your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride on rollercoaster.")
    age = int(input("What's Your age? "))
    if age < 12:
        print("Rollercoaster ride charge is $5")
        bill = 5
    elif age >12 and age <18:
        print("Rollercoaster ride charge is $7")
        bill = 7
    else:
        print("Rollercoaster ride charge is $12")
        bill = 12
    photos = input ("Do You wanna take Photos: Y or N/ ")
    if photos== 'Y':
        print("Extra 3$ charged.")
        bill +=3
    else:
        print("Thank You for our services.")
    print(f"Your total bill is ${bill} ")

else:
    print(f"Sorry, your height is {height}, The minimum height required to ride the rollercoaster is 120 cm")
