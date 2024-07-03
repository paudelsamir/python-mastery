
from art import logo
clear = lambda: print("\033c", end="", flush=True) #This is the funciton for clearing the console
print (logo)

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
yes = True
while yes:
    bids= {}
    name = input("What's your name? ")
    price = float(input("What's your bid price? "))
    bids[name]= price

    choice = input("Are there any other users? Y/N \n").lower()
    if choice == "n":
        
        yes = False
    elif choice == "y":
        clear()
find_highest_bidder(bids)