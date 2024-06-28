from menu import MENU, resources

profit = 0.0

def calculate_coins():
    try:
        quarters = int(input("How many 25 cents coins you want to insert? ")) * 0.25
        dimes = int(input("How many 10 cents coins you want to insert? ")) * 0.10
        nickels = int(input("How many 5 cents coins you want to insert? ")) * 0.05
        pennies = int(input("How many 1 cents coins you want to insert? ")) * 0.01
        total_insert = quarters + dimes + nickels + pennies
        return round(total_insert, 2)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0.0

def total_return(total_insert, coffee_cost):
    if total_insert == coffee_cost:
        return "Your inserted coins match the coffee value."
    elif total_insert > coffee_cost:
        to_return = round((total_insert - coffee_cost), 2)
        return f"Here is your return: ${to_return}"
    elif total_insert < coffee_cost:
        return f"Insufficient funds. {choose_coffee}'s price is ${coffee_cost}."

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True
while is_on:
    choose_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choose_coffee == "off":
        is_on = False
    elif choose_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    elif choose_coffee in MENU:
        drink = MENU[choose_coffee]
        coffee_cost = drink["cost"]
        
        if check_resources(drink["ingredients"]):
            total_insert = calculate_coins()
            print(f"You Inserted: ${total_insert}")
            
            if total_insert >= coffee_cost:
                print(total_return(total_insert, coffee_cost))
                make_coffee(choose_coffee, drink["ingredients"])
                profit += coffee_cost 
            else:
                print(total_return(total_insert, coffee_cost))
        else:
            print("Unable to make the drink. Please choose another option.")
    else:
        print("Invalid selection. Please choose from espresso, latte, cappuccino")
