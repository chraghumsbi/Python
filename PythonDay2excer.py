# First excerise
number = input('Type a two digit number:')
print(type(number))
f1 = number[0]
f2 = number[1]

final_result = int(f1)+int(f2)
print(final_result)

# second excersie

height = input('Enter your height in m: ')
weight = input('Enter your weight in kg:" ')
# print(type(height))
# print(type(weight))

height = float(height)
weight = int(weight)

bmi = weight/height ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

# Your life in Weeks

age = input('What is current age: ')
years = input('How many year you want to live: ')
age_as_int = int(age)
total_years = int(years)
years_remaining = total_years-age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f'You have {days_remaining} days,{weeks_remaining} weeks, {years_remaining} Years'
print(message)
