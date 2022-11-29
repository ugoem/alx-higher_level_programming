#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Find the last digit
def lastDigit(number):
  return (number % 10)

if lastDigit(number) > 5:
   print(f"Last digit of {int(number)} is {int(lastDigit(number))} and is greater than 5")
elif lastDigit(number) == 0:
  print(f"Last digit of {int(number)} is {int(lastDigit(number))} and is zero")
elif lastDigit(number) < 6 and lastDigit(number) != 0:
  print(f"Last digit of {int(number)} is {int(lastDigit(number))} and is less than 6 not 0")
