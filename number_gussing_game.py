
import random, math

# Take first input from users
lower = int(input('Enter the lower number:'))

# Take second input from users
upper = int(input('Enter the upper number: '))

# Generating number between lower and upper
number = random.randint(lower, upper)

# Initializing the number of guesses
count = 0

# For calculation of minimum number of guessess depends upon range
while count < math.log(upper - lower, 2):
    count += 1

    # taking gussing number as input from user
    guess = int(input('Guess the number: '))
    if number == guess:
        print('Right answer', guess)
        break
    elif number > guess:
        print('You guess to small! try again')
    elif number < guess:
        print('You guess to large! try again')
