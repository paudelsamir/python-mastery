row1 = ["🩶","🩶","🩶"]
row2 = ["🩶","🩶","🩶"]
row3 = ["🩶","🩶","🩶"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Enter the positon where you want to put the treasure: ")

#If we type 12
#position[0]= 1    row/ horizontal
#position[1]= 2    column/ vertical

horizontal = int(position[0])
vertical = int(position[1])

mappedrow = map[horizontal-1] #first we go to row and then we select the column where the changes to be made.
mappedrow[vertical-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
