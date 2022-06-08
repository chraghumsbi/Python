# Data Types

# string

from cgi import print_environ
from numpy import true_divide


print('Hello'[0])
print('Hello'[:-1])
print('12345'[:-1])
print('Hello'[:-1]+'12345'[:-1])

# integers
i = 123
b = 234
print(f'first number {i} and second number {b}')
print(i)
print(b)


# float

a = 2.4344
b = 3.6434
print(round(a+b, 3))

# boolean

a = 'abc'
b = 'abe'
a == b

# length

a = len(input('what is yout name?'))
print(f' your name total characters: {a}')

# Matthematics

# PEMDAS
# ()
# **
# *
# /
# +
# -
# # real time calculation order like */+-
# */ same priorty and then based on () take it from left to right
# 1
print(3*3+3/3-3)

# 2
print(3*3+(3+3)/3-3)

# Round
print(round(89/54, 3))

result = 6/3
result /= 2
print(result)

score = 9
height = 1.8
iswinning = True
# f-string
print(f' Your score {score} and height {height} and isWinnig {iswinning}')

print(6 + 4 / 2 - (1 * 2))

ad = int("5") / int(2.7)
print(type(ad))
