# Hangman Game
# We are developing a hangman game. 
# Here, we will be:
# 1. choosing a word from list of words.
# 2. now user needs to identify or guess the word by guessing the letters in the word.
# 3. user will have some chances to guess the word.

import random

# ascii art
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
# earlier it was a string but now it is a list of words, becoz of split.
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
# We will not show the choosen word to user, this is for test cases only.
# print(f"The chosen word is {chosen_word}.")

# Learning Point:
# ''' ''' is used for multi-line string or docstring. It can also be used for single line string, but it is not a good practice. 
# Docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. It is used to document the code.
# When python encounters a ''' ''' it creates a string object and if its not assigned to any variable then it is ignored by Python.
'''
gh
'''

# Now, we need to show encrypted word with _ instead of actual word.
guess_word = []
# for letter in chosen_word:
#     guess_word.append("_")
guess_word = ["_"] * len(chosen_word)
guessWord = " ".join(guess_word) #will join the list items with space in between, so that it will look like _ _ _ _ _ instead of _____ .
print(" ".join(guess_word)) # _ _ _ _ _

# we should be guessing letter either
# 1. chances exhaust [7 chances]
# 2. word guessed correctly
chances = 0
guess_right = set()
while "".join(guess_word) != chosen_word:
    # guess, let user guess a letter
    guess = input("Save hangman, guess a letter: ").lower()
    # This block is to check if user is guessing same letter again or not.
    if guess in guess_right:
        print("You already guessed this letter, try another one.")
        continue
    guess_right.add(guess)
    right_guess = False
    # instead of me handling index and value by itself, use enumerate it will give and handle index and value both.
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            right_guess = True
            guess_word[i] = guess
            print(" ".join(guess_word))
    if right_guess == False:
        # this letter is not in the word, chances increase by 1
        # Either this 
        # print(f"Wrong guess {HANGMANPICS[chances]}")
        # or simply print hangmanpics 
        print(HANGMANPICS[chances])
        chances += 1
        if chances == 7:
            print("You loose!!!")
            break
if "".join(guess_word) == chosen_word:
    print('''Congrats!!!
          You saved hangman!!!''')
print("Game Over!!!")
