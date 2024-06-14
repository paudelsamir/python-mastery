sum = 0
for num in range(1,101): #you can do it in a differenct appproach like for num in range(1,101,2)
    if num %2 == 0:
        even_num = num 
        sum = sum+even_num #
print (sum)# Printing ouside the for loop give only the aggregated sum whereas printing inside the loop give all steps