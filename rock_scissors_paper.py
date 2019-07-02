import random

list = ['rock', 'paper', 'scissors']

player = input('rock, paper or scissors ?')
computer = random.choice(list)

if player == computer:
    print('DRAW!')

elif player == 'rock' and computer == 'scissors':
    print('Player wins!')

elif player == 'rock' and computer == 'paper':
    print('Computer wins!')

elif player == 'paper' and computer == 'rock':
    print('Player wins!')

elif player == 'paper' and computer == 'scissors':
    print('Computer wins!')

elif player == 'scissors' and computer == 'paper':
    print('Player wins!')

elif player == "scissors" and computer == 'rock':
    print('Computer wins!')

else:
    print('?????')
