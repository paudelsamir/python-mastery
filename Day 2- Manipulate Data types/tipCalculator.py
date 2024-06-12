print("Welcome to tip calculator ")
BILL = input("What was the total bill? $")
bill = float(BILL)
TIPP= input("What percentage tip would you like to give? 10, 12 or 15?")
tip_percentage = int(TIPP)
total_bill = bill+ bill* tip_percentage/100
SPLIT = input("How many people to split the bill? ")
split_to = int(SPLIT)
bill_per_person = total_bill/split_to
# final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
 