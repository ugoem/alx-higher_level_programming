#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lnumber = abs(number % 10)
if (lnumber > 5):
    print(f"Last digit of {number} is {lnumber} and is greater than 5")
elif (lnumber == 0):
    print(f"Last digit of {number} is {lnumber} and is 0")
elif (lnumber < 6 and lnumber != 0):
    print(f"Last digit of {number} is {lnumber} and is less than 6 not 0")
