#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)

print(chosen_word)

placeholder = ""
for i in range(chosen_word_len):
    placeholder += "_"
print(placeholder)


game_over = False

correct_letters = []
while not game_over:
    display = ''
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")

