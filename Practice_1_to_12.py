# Practice the concepts from Day 1 to Day 12
# practice use only sundays...
# Variables
my_learn = 'I am learning my python programing!'
print(my_learn)
a = 1
b = 2
c = a+b
print(c)
print(type(c))

# round
a = 2.345
b = 3.544
print(round(a+b, 2))
print(a == b)

result = a/b
result += 2
print(round(result, 3))

# adding two digit number
number = input('Enter two digit number: ')
f1 = number[0]
f2 = number[1]
result = int(f1)+int(f2)
print(result)

# Bmi Calculator

h = input('Enter your height in m: ')
w = input('Enter your weight in kg\'s:')

h = float(h)
w = int(w)
bmi = w/h**2
print(type(bmi))
bmi = round(bmi, 0)
print(f' Your BMI results: {bmi}')


# your life in weeks

current_age = int(input('Enter your current age: '))
years_remaining = int(input('How many years do you want to live: '))
total_remain_years = years_remaining-current_age
total_days_remain = total_remain_years*365
total_weeks_remain = total_remain_years*52
total_months_remain = total_remain_years*12
mesage = f'You have {total_remain_years} years and {total_months_remain} months and {total_weeks_remain} weeks and {total_days_remain} days.'
print(mesage)

# Restarant tip calculator

bill_amount = float(input('Enter bill amount: '))
tip_mode = input(
    'How much tip do you want to give like 10 ,20 or 30 in percentages or ruppes Type \'%\' or Type \'@\' ')
tip_amount = input('Enter your tip amount: ')
peoples = int(input('How many members attended: '))

if tip_mode == '%':
    tip = int(tip_amount)/100
    total_bill = bill_amount*tip
    total_bill = total_bill+bill_amount

else:
    tip = int(tip_amount)
    total_bill = bill_amount+tip

bill_per_people = total_bill/peoples
final_amount = round(bill_per_people, 2)
print(f'Each person should pay: {final_amount}')

# RoadCoaster

height = int(input('Hey buddy enter your height in cm: '))

if height > 120:
    age = int(input('Enter your age: '))
    if age < 7:
        bill = 5
        print(f'Hey buddy  your ticket cost: ${bill}')
    elif age >= 7 and age < 18:
        bill = 7
        print(f'Hey buddy  your ticket cost: ${bill}')
    elif age > 18 and age < 35:
        bill = 10
        print(f'Hey buddy  your ticket cost: ${bill}')
    else:
        bill = 15
        print(f'Hey buddy  your ticket cost: ${bill}')
    you_like_photo = input(
        'Hey buddy do you like photo on Roadcoaster Type \'Yes\' to take else Type \'No\' to not interested').lower()
    if you_like_photo == 'yes':
        bill += 3
        print(f' Hey buddy your total amount is: {bill}')
else:
    print('Hey buddy sorry for not having height.. try to do some excerise to grow height...')
