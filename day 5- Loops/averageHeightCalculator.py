list = input("Enter the heights seperated by a space: ").split( )
#height[0]= int(height[0])
# print(list)

heights = [int(height) for height in list]
print(heights)

# print(len(heights))
# print (sum(heights))
total_sum = 0
for height in heights:
    total_sum += height

# print(total_sum)

total_num = 0
for height in heights:
    total_num+=1

# print(total_num)

average_height= total_sum/total_num
print (average_height)