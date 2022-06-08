# # PythonDay4 execercise-1
# import random
# from traceback import print_tb
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print('Heads')
# else:
#     print('Tails')

# # PythonDay4 execercise-2
# # list
# # Split string method
# # we can use Random
# import random
# name = input('Give me the everybody credit cards by owners: ')
# name = name.split(', ')
# name_len = len(name)  # get the total numbers of list
# random_choise = random.randint(0, name_len-1)
# person_who_will_pay = name[random_choise]
# print(f'{person_who_will_pay} is going to buy meals for us.. ')

# PythonDay4 execercise-3
# # Treasure Map
# from turtle import position


# row1 = ['☑️', '☑️', '☑️']
# row2 = ['☑️', '☑️', '☑️']
# row3 = ['☑️', '☑️', '☑️']

# map = [row1, row2, row3]
# print(f'\n{row1}\n{row2}\n{row3}')
# position = input('Where do you want to put the treasure? ')

# horizontal1 = int(position[0])
# vertical1 = int(position[1])

# selected_row = map[vertical1-1]
# selected_row[horizontal1-1] = '🗳️'

# print(f'\n{row1}\n{row2}\n{row3}')

# PythonDay4 execercise-4
# Rock, paper and Scissors


import random
# from PIL import Image

# rock = Image.open("C:\\Users\\chrag\\Downloads\\images_rock.jpg").show()

# paper = Image.open("C:\\Users\chrag\\Downloads\\images_paper.jpg").show()

# scissors = Image.open(
#     "C:\\Users\\chrag\\Downloads\\images_scissors.jpg").show()
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper,2 for scissors.\n'))
print('User Chose: ')
if user_choice >= 3 or user_choice < 0:
    print('You typed an invalid number..')
else:
    print(game_images[user_choice])

computer_choise = random.randint(0, 2)
print('Computer chose: ')
print(game_images[computer_choise])
if user_choice == 0 and computer_choise == 2:
    print('You Win!')
elif computer_choise == 0 and user_choice == 2:
    print('You lose!')
elif computer_choise > user_choice:
    print('You lose!')
elif user_choice > computer_choise:
    print('You Win!')
elif computer_choise == user_choice:
    print('It\'s draw!')
