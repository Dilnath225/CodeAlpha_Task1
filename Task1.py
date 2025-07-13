"""Hangman Game in Python
This is a simple implementation of the classic Hangman game.
Players guess letters to figure out a hidden word, with a limited number of incorrect guesses allowed.

Author: Rathnayaka Pathiranage Sunera Dilnath
Student ID: CA/JU1/26435
Date: 2025- 07-11
Location: Sri Lanka

"""

import random

def hangman():

    word_lst = [apple, banana, cherry, date, chair]
    word = random.choice(word_lst)

    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))  #displaying blanks for each letter in the word


    #creating game loops
    while incorrect_guesses < max_attempts:
        guess = input("\nGuess a letter: ").lower()

        