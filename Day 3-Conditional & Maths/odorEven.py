num = int(input("Which Number do you want to find whether it is odd or even? "))
remainder = num % 2
if remainder == 0:
    print("The given number is even. ")
else:
    print("The given number is odd. ")