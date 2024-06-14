
# Fizz for Numbers divisible by 3
# Buzz for Numbers divisible by 5
# FizzBuzz for numbers divisible by 3 as well as 5

# It Might Start off like this:
"""
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

"""
num = 0
for num in range(1,100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizBuzz")
    elif num % 3 == 0 :
         print("Fizz")
    elif num % 5 ==0:
        print("Buzz")
    else:
        print(num)