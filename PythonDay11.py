# Day 11
# blackjack Project

import random as rd
import os
from PythonDay11excercise_art import logo


def deal_card():
    """
    Return random card from deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rd.choice(cards)
    return card


def cal_score(cards):
    """
    Take  a list of cards and return score of calculate cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def clear():
    '''
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful for managing
    menu screens in terminal applications.
    '''
    os.system('cls||echo -e \\\\033c')


def compare(u_sc, c_sc):
    """
    Takes scores from user and computer and return the results
    """
    if u_sc == c_sc:
        return 'Draw 😊'
    elif c_sc == 0:
        return 'Lose, oppenet has Blackjack 😂'
    elif u_sc > 21:
        return 'You went over.. You lose 😢'
    elif u_sc == 0:
        return 'You win a Blackjack 😎'
    elif c_sc > 21:
        return 'Your opponent went over.. You win 😎'
    elif u_sc > c_sc:
        return 'You win a Blackjack 😎'
    else:
        return 'You lose 😢'


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = cal_score(user_cards)
        computer_score = cal_score(computer_cards)
        print(f' Your cards: {user_cards},current score: {user_score}')
        print(f' Computer first  cards: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_next_deal = input(
                " Type 'Yes' to get another card. or Type 'No' to pass: ").lower()
            if user_next_deal == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = cal_score(computer_cards)
    print(f' Yout final hand: {user_cards}, final score: {user_score}')
    print(
        f' computer final hand: {computer_cards}, final score: {computer_score}')
    print(compare(user_score, computer_score))


while input('Do you want play a game of Blackjack? Type \'y\' to contine or Type \'n\' to drop: ') == 'y':
    clear()
    play_game()
