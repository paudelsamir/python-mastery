#Basically This program takes your name and your crush's name and calculate the number of t,r,u,e and l,o,v,e in their name and 
#append the both sum by making it a stirng to show the love in respect of number.

print("Welocme to the love calulator: ")
name1 = input("What is your name? ")
name2 = input("What's his/her name? ")
name = name1+name2
lowercase_name =name.lower()


T = lowercase_name.count('t')
R = lowercase_name.count('r')
U = lowercase_name.count('u')
E = lowercase_name.count('e')

L = lowercase_name.count('l')
O = lowercase_name.count('o')
V = lowercase_name.count('v')
E = lowercase_name.count('e')

true = str(T+R+U+E)
love = str(L+O+V+E)

total = true+love
print(total)