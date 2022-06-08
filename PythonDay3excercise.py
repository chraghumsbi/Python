# Day3 python excercise:1
from numpy import bmat


number = int(input('Which number do you want to check: '))
result = number % 2
if result == 0:
    print('This is Even number')
else:
    print('This is Odd number')


# Day3 python excercise:2

h = float(input('Enter your height in m: '))
w = float(input('Enter your weight in kg: '))

bmi = round(w/h**2)
if bmi < 18.5:
    print(f'your bmi is {bmi}, you are underweight')
elif bmi >= 18.5 and bmi < 25:
    print(f'your bmi is {bmi}, you are normalweight')
elif bmi >= 25 and bmi < 30:
    print(f'your bmi is {bmi}, you are overweight')
elif bmi >= 30 and bmi < 35:
    print(f'your bmi is {bmi}, you are obese')
else:
    print(f'your bmi is {bmi}, you are clinically obese')


# Day3 python excercise:3
year = int(input('Which year you want to check: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('It''s leap year!')
        else:
            print('It''s notmal year!')
    else:
        print('It''s leap year!')
else:
    print('It''s notmal year!')
