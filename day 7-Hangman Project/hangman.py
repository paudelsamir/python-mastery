import random

words = 'ant babboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole rat raven rhino shark sheep spider toad turkey turtle wolf wombat zebra'
words_list =words.split(" ")
# print(words_list)
# print(words_list[5])

random_word =random.choice(words_list) 
print(random_word)

to_fill = ""
for alphabets in random_word:
    to_fill = to_fill + "_"
print(to_fill)

life = len(random_word)
# guess_letter = input("Please guess the letter: ").lower()

          








for letter in to_fill:
    print(f"Your Lives remaining is {life}")
    guess_letter = input("Please Guess the letter: ").lower()
    for letter in random_word:
        if letter == guess_letter:
            for dyaas in to_fill:
                dyass = guess_letter
            print(guess_letter)
            to_fill = to_fill + guess_letter
        else:
            print("_")
            life -= 1   
            if life ==  0:
                print(f"Game Over! Your Lives remaining is{life}")
    

