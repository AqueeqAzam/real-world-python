# initializing phase
total = 0
grade_counter = 0
grades = [98, 34, 65, 87, 78, 65, 44, 54, 94, 75]

# processing phase
for grade in grades:
    total = total + grade
    grade_counter = grade_counter + 1

# termination phase
average = total / grade_counter
print('class average is:', average)
if average >= 40:
    print('passed')
else:
    print('failed')

