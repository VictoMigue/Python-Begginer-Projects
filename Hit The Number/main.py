from random import randint
from os import system

computer = randint(1, 100)
attempts = 0

print('I thought of a number from 1 to 100, try to hit it!')

system('pause')
system('cls')

while True:
    player = int(input('Try hit:'))

    if player == computer:
        break
    if player > computer:
        print('Try using a smaller number!')
        attempts += 1
    else:
        print('Try using a bigger number!')
        attempts += 1
    system('pause')
    system('cls')

print('Good job!')
print(f'The number was {computer}!')
print(f'With {attempts} attempts!')