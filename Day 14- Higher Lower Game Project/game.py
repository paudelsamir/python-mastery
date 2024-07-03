import random
from art import logo, vs
from data import data

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"name: {name}\n description: {description}\n country: {country}\n"

def compare_followers(account1, account2):
    follower1 = account1['follower_count']
    follower2 = account2['follower_count']
    if follower1 > follower2:
        return 'a'
    else:
        return 'b'

def game():
    print(logo)
    score = 0
    should_continue = True
    account1 = get_random_account()
    account2 = get_random_account()
    
    while should_continue: 
        account1 = account2
        account2 = get_random_account()
        
        while account1 == account2:
            account2 = get_random_account()
        
        print(f"Compare A: {format_data(account1)}")
        print(vs)
        print(f"Against B: {format_data(account2)}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = compare_followers(account1, account2)
        
        if guess == correct_answer:
            score += 1
            print(f"Correct! Current score: {score}")
        else:
            print(f"Wrong answer. Final score: {score}")
            should_continue = False

game()
