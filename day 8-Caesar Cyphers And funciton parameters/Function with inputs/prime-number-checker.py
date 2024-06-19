def prime_checker(number):
    if number % 2 == 0:
        print(f"The number {number} is prime number.")
    else:
        print(f"The number {number} is not a prime number.")
 
n = int(input("Enter number you want to check: ")) 
prime_checker(n)