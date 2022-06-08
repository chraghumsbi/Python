
print('Welcome to Love Calculator')
name_men = input('What is your name? \n')
name_women = input('What is your name? \n')

name_m = name_men.lower()
name_w = name_women.lower()
final_name = name_m+name_w
print(final_name)
t = final_name.count('t')
r = final_name.count('r')
u = final_name.count('u')
e = final_name.count('e')
true = t+r+u+e
l = final_name.count('l')
o = final_name.count('o')
v = final_name.count('v')
e = final_name.count('e')

love = l+o+v+e

love_score = true+love

if love_score < 10 or love_score > 90:
    print(
        f'Your love score is {love_score}, you go together like coke and mentos ')
elif love_score >= 40 or love_score <= 50:
    print(f'Your love score is {love_score}, you are alright together ')
else:
    print(f'Your love score is {love_score}')
