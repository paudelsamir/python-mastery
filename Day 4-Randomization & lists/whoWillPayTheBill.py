
import random
names= input("Give me everybody's name separated by a comma/ ")
name_list = names.split(",")
print(name_list)

ran =random.randint(0,3)

going_to_pay = name_list[ran]

print(going_to_pay+ " is going to pay the bill")
