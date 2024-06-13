weight = input("Enter Your weight in kg ")
height = input("Enter the height in m ")

BMI = int(weight)/float(height) ** 2
bmi = int(BMI) 
print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are Underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, You have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, You are Overweight")
elif bmi >30 and bmi < 35:
    print(f"Your BMI is {bmi}, You are Obese")
else:
    print(f"Your BMI is {bmi}, You are Clinically Obese")