print('Welcome to tip calculator!')
bill = float(input('what was the total bill?$'))
tip = int(input('How much tip would you like to give? 10,15 or 20'))
peoples = int(input('How many peoples split bill?'))

tip_as_per = tip/100
total_tipamount = bill*tip_as_per
total_bill = bill+total_tipamount
bill_per_person = total_bill/peoples
final_amount = round(bill_per_person, 2)

print(f'Each person should pay ${final_amount}')
