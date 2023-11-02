import random

number = random.randint(1, 100)
while True:
    guessed_number = int(input('Guess the number: '))
    if guessed_number < number:
        print('Too small!')
    elif guessed_number > number:
        print('Too big!')
    elif guessed_number == number:
        print('You win!')
        break
