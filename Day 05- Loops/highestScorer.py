student_scores = input("Enter the scores of a class separated by a space: ").split( )
for n in range (0, len(student_scores)):
    student_scores[n]= int (student_scores[n])
print(student_scores)

highest_score = student_scores[0]
#Logic for Printing the highest score, compare two scores side by side as well as assign the highest score through iterations:
for n in range(1, len(student_scores)):
    if(student_scores[n] > highest_score):
        highest_score = student_scores[n]
        
print(f"The highest marks is {highest_score}")


