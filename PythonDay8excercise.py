# # Day 8 Area calculator Excercise
# import math


# def paint_cal(height, width, coverage):
#     area = height*width
#     num_of_cans = math.ceil(area/coverage)
#     print(f'You wulll need {num_of_cans} cans of paint the wall')


# test_height = int(input('Height of the wall: '))
# test_width = int(input('width of the wall: '))
# coverage = 5

# paint_cal(height=test_height, width=test_width, coverage=coverage)


# Prime numbers

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('It\'s a prime number .')
    else:
        print('It\'s not a prime number')


num = int(input('Check this number: '))

prime_checker(number=num)
