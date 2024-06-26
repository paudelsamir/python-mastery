from art import logo

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    
    print(logo)
    first = float(input("Enter First Number: "))
    for operators in operations:
        print(operators)
    print("\n")
    


    choice = 'Y'
    while choice:
        if choice == 'Y':
            operation_symbol = input("Enter Operation Symbol: ")
            next = float(input("Enter Next Number please: "))
            function = operations[operation_symbol]
            answer = function(first, next)
            print(f"{first} {operation_symbol} {next} = {answer}")
        
            choice = input(f"Type 'y' to continue calculating with {answer}, Type 'n' for new calculation or exit: ").upper()
            first = answer
        else:
            exit_cal = input("Type 'y' for new calculation, type 'n' for exit ").upper()
            if exit_cal == 'N':
                print("\nThankyou for using Calculator 2.0")
                exit()
            else:
                calculator()
calculator()
    