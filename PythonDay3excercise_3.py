print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('Welcome to Tresure Island')
print('Your mission is to find the treasure')
choise1 = input(
    'You are at a crossroad, where do you want to go? Type "Left" or "Right".').lower()
if choise1 == 'left':
    choise2 = input(
        ' you\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait fot a boat. Type "Swim" to swim across.').lower()
    if choise2 == 'wait':
        choise3 = input(
            'You arrive the island unharmed.. There is a house with 3 doors. one red , one yellow and blue... Which colour do you choose?').lower()
        if choise3 == 'red':
            print('It\'s a room full of fire.. Game over')
        elif choise3 == 'yellow':
            print('Yah! you found the treasure! you won! Congratulations ')
        elif choise3 == 'blue':
            print('You\'ve entered a room of beasts.. Game over')
        else:
            print('You chose a door that doesn\'t exit.. Game over..')
    else:
        print('You got attacked by an trout. Game over..')
else:
    print('Game is over..')
