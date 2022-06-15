# Odd or Even number checker
number = int(input('Which number do you want to check'))
if number % 2 == 0:
    print(f' Number:{number} is Even ')
else:
    print(f' Number:{number} is Odd ')

# Leap number excercise:

year = int(input('Which year do you want to check'))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f' The year {year} is leap year!')
        else:
            print(f' The year {year} is Not leap year!')
    else:
        print(f' The year {year} is leap year!')
else:
    print(f' The year {year} is Not leap year!')


# Fizz Buzz game
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
