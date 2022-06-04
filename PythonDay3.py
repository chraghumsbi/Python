# Control flow in python
print('Welcome to my bike')
height = int(input('What is your height in cm: '))

if height >= 120:
    print('Ya! Welcome to roadcoster!')
    age = int(input('Enter your age: '))
    if age < 12:
        print('Hey buddy your ticket cost is: $5')
    elif age >= 12 and age < 18:
        print('Hey buddy your ticket cost is: $7')
    else:
        print('Hey gentle man your ticket cost is: $10')
else:
    print('Sorry, please grow your height and come back.. Thank you!')


# comparison Operators
# <
# >
# >=
# <=
# ==
# !=
