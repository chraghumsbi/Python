# Guessing Number

import random
from PythonDay12_art import log
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def clear():
    '''
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful for managing
    menu screens in terminal applications.
    '''
    os.system('cls||echo -e \\\\033c')
# function to get the user guess against  actual answer


def check_answer(guess, answer, turns):
    """
    Checks answer against guess and remaining turns
    """
    if guess > answer:
        print('Too High')
        return turns-1
    elif guess < answer:
        print('Too Low')
        return turns-1
    else:
        print(f'Yeah you guessed and correct answer was {answer}')
        user = input('Do you want play again! Type \'y\' or Type \'n\'. ')
        if user == 'y':
            game()
        else:
            clear()


def set_diffculty():
    level = input('Choose a difficulty. Type \'easy\' or \'hard\':').lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(log)
    print('Welcome to the Number guess game')
    print('I\'m thinking number from 1 to 100')

    answer = random.randint(1, 100)
    print(f' The correct answer is {answer}')

    turns = set_diffculty()
    # print(f' You have {turns} attemps remaing to guess the number. ')

    guess = 0
    while guess != answer:
        print(f' You have {turns} attemps remaing to guess the number. ')
        guess = int(input('Make a guess: '))
        turns = check_answer(guess=guess, answer=answer, turns=turns)
        if turns == 0:
            print(f' You\'ve run out of guesses, you lose.')
            if input('Do you want play again! Type \'y\' or Type \'n\'. ') == 'y':
                game()
            else:
                clear()
                return
        elif guess != answer:
            print('Guess again')


game()
