# Loops using student height scores
student_scores = input('List of students scores: ').split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

print(max(student_scores))
print(min(student_scores))

height_score = 0
for score in student_scores:
    if score > height_score:
        height_score = score
print(f'Students height score: {height_score}')

# # Loops Range function
totals = 0
for number in range(1, 101):
    # print(number)
    totals += number
print(totals)

# Adding even numberse
total_evens = 0
for evennumbers in range(1, 101):
    if evennumbers % 2 == 0:
        total_evens += evennumbers
print(total_evens)

# Loops Fizz Buzz game

for game in range(1, 101):
    if game % 3 == 0 and game % 5 == 0:
        print('FizzBuZZ')
    elif game % 3 == 0:
        print('Fizz')
    elif game % 5 == 0:
        print('Buzz')
    else:
        print(game)
