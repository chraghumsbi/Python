# loopss
from audioop import avg


student_heights = input('Input a list of student heights ').split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)
# total_height = sum(student_heights)
# total_no_of_students = len(student_heights)
# avg_height = round(total_height/total_no_of_students)
# print(avg_height)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
total_no_of_students = 0
for lenth in student_heights:
    total_no_of_students += 1
print(total_no_of_students)
avg_height = round(total_height/total_no_of_students)
print(f' Average students heights: {avg_height}')
