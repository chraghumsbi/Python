# PythonDay7 for &while and if/else/elif, strings lists ranges and modules
# Hangman game using python
import random

# word_list = ['Amma', 'Nana', 'wife', 'daughter']
import Hangman_art
import Hangman_wordlist

print(Hangman_art.logo)

chosen_word = random.choice(Hangman_wordlist.word_list).lower()
live = 6
print(f'passt , the solution is {chosen_word}')
chose_word_blank = []
for _ in range(len(chosen_word)):
    chose_word_blank += '_'
print(chose_word_blank)
end_of_game = False

while not end_of_game:
    user_input = input('guess a letter: ').lower()

    if user_input in chose_word_blank:
        print(f' Heyy congratulations your guess  is there in word')
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_input:
            chose_word_blank[position] = letter

    if user_input not in chosen_word:
        print(f' You chosen word nor present the word!')
        live -= 1
        if live == 0:
            end_of_game = True
            print('You lose')
    print(chose_word_blank)

    if '_' not in chose_word_blank:
        end_of_game = True
        print('You Win!')
    print(Hangman_art.stages[live])
