#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[random.randint(0, len(word_list)-1)]

print(chosen_word)
print(len(chosen_word))
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Letter?")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
i = 0
#while i < len(chosen_word):
#    if guess == chosen_word[i]:
#        print("Right")
#    else:
#        print("Wrong")
#    i+= 1
