AGE = input("Enter your current age in years: ")
age = int(AGE)

year_remaining = 90 - age
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remaining = year_remaining * 12

print(months_remaining)

message = f"You have {days_remaining} days,{weeks_remaining} weeks, and {months_remaining} months left"
print(message)