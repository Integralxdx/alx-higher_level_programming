#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if number < 10:
    lastDigit = number % -10
print(f"Last digit of {number:d} is {lastDigit:d} and is ", end="")
if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
