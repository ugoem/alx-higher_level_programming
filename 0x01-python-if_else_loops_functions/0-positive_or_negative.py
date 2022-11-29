#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{int(number)} is positive")
elif number == 0:
    print(f"{int(number)} is zero")
elif number < 0:
    print(f"{int(number)} is negative") 
