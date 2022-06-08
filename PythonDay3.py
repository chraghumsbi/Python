# Control flow in python
print('Welcome to my bike')
height = int(input('What is your height in cm: '))

if height >= 120:
    print('Ya! Welcome to roadcoster!')
    age = int(input('Enter your age: '))
    if age < 12:
        bill = 5
        print('Hey buddy your ticket cost is: $5')
    elif age >= 12 and age < 18:
        bill = 7
        print('Hey buddy your ticket cost is: $7')
    else:
        bill = 10
        print('Hey gentle man your ticket cost is: $10')
    you_likephoto = input('Do you want photo? Y or N ')
    if you_likephoto == 'Y':
        bill += 3
        print(f'Your final ticket price is : ${bill}')
else:
    print('Sorry, please grow your height and come back.. Thank you!')


# comparison Operators
# <
# >
# >=
# <=
# ==
# !=
