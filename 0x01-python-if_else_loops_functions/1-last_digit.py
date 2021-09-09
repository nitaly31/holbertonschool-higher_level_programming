#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {:d} is {:d} and is less than 6 and not 0"
if number >= 0:
    ld = number % 10
else:
    ld = number % -10

if(number > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, ld))
elif (number == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, ld))
else:
    print(str.format(number, ld))
