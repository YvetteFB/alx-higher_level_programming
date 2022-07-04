#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = number % 10
print(f'The last digit of {number} is {rem}', end="")
if rem > 5:
    print(f'and is greater than 5')
elif rem == 0:
    print(f'and is 0')
else:
    print('and is less than 6 and not 0')
