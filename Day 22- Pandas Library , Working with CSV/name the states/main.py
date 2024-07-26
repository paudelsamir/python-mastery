import pandas as pd

# Read the CSV file
data = pd.read_csv('Day 22- Pandas Library , Working with CSV/name the states/50_states.csv')

# Access the blank_states_img.gif file
image_path = r'C:\Users\samir\GitHub\python-mastery\Day 22- Pandas Library , Working with CSV\name the states\blank_states_img.gif'

with open(image_path, 'rb') as image_file:
    # Perform operations on the image file
    # Add your code here to perform operations on the image file
    # ...
    
    # Guess the state
    guess = input("Guess the state: ")
    
    # Check if the guess is correct
    if guess in data['state'].values:
        # Show the state name on the map
        state_name = data.loc[data['state'] == guess, 'state_name'].values[0]
        print(f"Correct! The state is {state_name}")
        
        # Continue the game
        # ...
    else:
        # Get all the state names
        state_names = data['state_name'].values
        
        # Find the closest state name to the incorrect guess
        closest_state_name = min(state_names, key=lambda x: abs(len(x) - len(guess)))
        
        print(f"Incorrect guess. The closest state is {closest_state_name}. Try again!")