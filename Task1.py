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

    word_lst = ['apple', 'banana', 'cherry', 'date', 'chair']
    word = random.choice(word_lst)

    guessed_lttrs = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))  #displaying blanks for each letter in the word


    #creating game loops
    while incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single letter.")
            continue

        if guess in guessed_lttrs:
            print("You already guessed that letter.")
            continue

        guessed_lttrs.append(guess)

        if guess in word:
            print(f"Good guess!.. the letter'{guess}' is in the word.")

        else:
            incorrect_guesses += 1
            print(f"Sorry...the letter '{guess}' is not in the word. You have {max_attempts - incorrect_guesses} attempts left.")

            # Displaying the current state of the word
            display_word =  ''
            for letter in word:
                if letter in guessed_lttrs:
                    display_word += letter + ' '
                else:
                    display_word += '_ '
            print(display_word.strip())

            #checking the word if guessed is right
        if all(letter in guessed_lttrs for letter in word):
            print(f"Congratulations!...You guessed the word '{word}' correctly!")
            break
    else:
        print(f"Sorry....you've run out of attempts. The word was '{word}'.")

        
#runnning the game
hangman()