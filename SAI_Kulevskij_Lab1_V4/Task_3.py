import random
import math

while True:
    your_number = int(input())
    mystery_number = int(random.randint(0, 9))

    if your_number == mystery_number:
        print(f'You passed! Your number is {your_number} equal to {mystery_number}')
    else:
        print(f'You failed! Your number is {your_number} not equal to {mystery_number}')