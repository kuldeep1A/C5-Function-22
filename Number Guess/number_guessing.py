import os
import time
from random import randint
from art import number_guess_logo


EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def clear(): return os.system('cls')


def check_answer(guess, answer, turns):
    """Check the answer against guess. Return the number of turns remaining."""
    if guess > answer:
        print("Too high. ")
        return turns - 1
    elif guess < answer:
        print("Too low. ")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURN
    elif level == 'hard':
        return HARD_LEVEL_TURN
    else:
        print("You type ? Please try again!")
        time.sleep(3)
        clear()
        game()


def game():
    print(number_guess_logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thingking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f"pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()
