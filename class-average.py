#----------------------------simple program to demostrate class average of class---------------------------------
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

# ---------------------------asking from user input------------------------------
# initialization phase
total = 0
grade_counter = 0

grades = int(input('Enter grade, -1 to end:'))

# processing phase
while grade != -1:
    total = total + grade
    grade_counter = grade_counter + 1
    grade = int(input('Enter grade, -1 to end:'))

# termination phase
    if grade !=0:
        average = total / grade_counter
        print('class average is', average)
    else:
        print('no grades were found')


# -----------------------break and coutinue statements-----------------------------
for number in range(100):
    if number == 11:
        break
    print(number, end= ' ')

for number in range(10):
    if number == 5:
        continue
    print(number, end=' ')

# ----------------------AND, OR and NOT statements-----------------------------------    
gender = 'Femail'
age = 70

if gender == 'Femail' and age == 55:
    print('senior femail')

if gender == 'Femail' or age == 26:
    print('Marred')

if not age == 45:
    print('she can birth')
