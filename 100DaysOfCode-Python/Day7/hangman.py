# Hangman Game
# We are developing a hangman game. 
# Here, we will be:
# 1. choosing a word from list of words.
# 2. now user needs to identify or guess the word by guessing the letters in the word.
# 3. user will have some chances to guess the word.

# To-Do
# 1. Randomly choose a word from the list of words word_list and assign it to a variable called chosen_word.
# 2. Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# 3. Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# 4. Print "Right" if the user got the letter right. Otherwise, print "Wrong".

# ascii art

import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Learning Point:
# We can do string concatenation like this
# print('hello '
#       'world')

# .split() method splits a string into a list. By default, it splits on whitespace - space, tab, newline.

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


print("Welcome to the Hangman Game!")

# we use .choice() method to randomly select an item from a list, tuple, or string.
chosen_word = random.choice(words)
print(f"The chosen word is {chosen_word}.")

# Now, we need to show encrypted word with _ instead of actual word.
guess_word = []
for letter in chosen_word:
    guess_word.append("_")
guessWord = " ".join(guess_word)
print(" ".join(guess_word)) # _ _ _ _ _

# we should be guessing letter either
# 1. chances exhaust [7 chances]
# 2. word guessed correctly
chances = 0
while "".join(guess_word) != chosen_word:
    # guess, let user guess a letter
    guess = input("Save hangman, guess a letter: ").lower()
    i = 0
    right_guess = False
    for letter in chosen_word:
        if letter == guess:
            right_guess = True
            print("found")
            guess_word[i] = guess
            print(f"{guess_word}")
        i += 1
    if right_guess == False:
        # this letter is not in the word, chances increase by 1
        print(f"Wrong guess {HANGMANPICS[chances]}")
        chances += 1
        if chances == 7:
            print("You loose!!!")
            break
if right_guess == True:
    print('''Congrats!!!
          You saved hangman!!!''')
print("Game Over!!!")
