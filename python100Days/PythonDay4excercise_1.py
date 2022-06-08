# Randoom password generators
import random


alphates = list(map(chr, range(65, 123)))
un_al = list(map(chr, range(91, 97)))
symbols = list(map(chr, range(32, 127)))
un_sym = [' ', '[', ']', '.', '\\', '>', '<', '{', '}', '|', '(', ')']
# print(un_sym)
num_1 = list(map(chr, range(48, 58)))
symbols_need = []
for i in un_al:
    alphates.remove(i)

for i in symbols:
    if i not in alphates:
        if i not in num_1:
            if i not in un_sym:
                symbols_need.append(i)


print('Welcome to Password Generator!')
user_letters = int(
    input('How many letters would you like in your password? \n'))
user_symbols = int(input('How many symbols would you like? \n'))
user_numbers = int(input('How many numbers would you like? \n'))

password_list = []
for char in range(1, user_letters+1):
    password_list += random.choice(alphates)
for char in range(1, user_symbols+1):
    password_list += random.choice(symbols_need)
for char in range(1, user_numbers+1):
    password_list += random.choice(num_1)

print(password_list)
random.shuffle(password_list)

password = ''
for i in password_list:
    password += i
print(f'Your password is: {password}')
