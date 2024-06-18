import random
from hangman_words import word_list
from ascii_art import stages, logo

print(logo)
print("\n\n")

random_word = random.choice(word_list)
print(random_word)

display = []
word_length = len(random_word)
for _ in range(word_length):
    display += "_"
# print(display)

lives = 5
end_of_game = False
while not end_of_game:
    guess_letter = input("Please guess the letter: ").lower()
    for position in range(word_length):
        letter = random_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess_letter}")
        if letter == guess_letter:
            display[position]= letter     
                                   
    

    print(f" ".join(display))
    print(f"\nGuessed letter: {guess_letter}")       
    
    if "_" not in display:
        end_of_game = True
        print("You won. Thank You for saving an innocent man from hanging.")    
        
    for position in range(word_length):
        letter = random_word[position]
        if letter == guess_letter:
            display[position] = letter

    if guess_letter not in random_word:
        lives -=1
        if lives > 0:
            print("The letter You guessed is not in the word!! be careful.")
        if lives == 0:
            end_of_game = True
            print("\nYou let a innocent man die!!")
            print(f"The Word to be guessed is {random_word}")
                           
    print(stages[lives])