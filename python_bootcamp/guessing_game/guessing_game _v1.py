import random

random_number = random.randint(1, 10) # numbers 1 - 10

guess = input("Pick a number from 1 to 10: ")
guess = int(guess)

if guess == random_number:
    print("YOU GOT IT!")
elif guess < random_number:
    print("TOO LOW!")
else:
    print("TOO HIGH!")

print(random_number)