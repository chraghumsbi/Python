print('Welcome to python pizza Delivery')
size = input('What size do you want: ')
pepper_required = input('Do you want pepper Y or N ')
cheese_requirred = input('Do you want cheese Y or N ')

bill = 0
if size == 'S':
    bill += 10
elif size == 'M':
    bill += 15
elif size == 'L':
    bill += 20
else:
    print('Please select size like S, M , L only')

if pepper_required == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
if cheese_requirred == 'Y':
    if size == 'S':
        bill += 1
    else:
        bill += 2
print(f'Your final bill is ${bill}')
