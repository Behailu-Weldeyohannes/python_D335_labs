
#  ********* Chapter Nine: Modules ********

"""
import arithmetic
import data

# def calculate(number):
#     return number - 3
# print(calculate(5))
# print(arithmetic.calculate(2))

# def calculate(number):
#     return number * 4

# print(calculate(5))
# print(arithmetic.calculate(5))

# def calculate(number):
#     return number + 2
# print(arithmetic.calculate(data.medium))
# print(calculate(data.medium))
import red
import green
import blue
import first
print(red.dark)
print(blue.dark)

def one(number):
    return number ** 2

def two(number):
    return number * 6

def three(number):
    return one(number) - two(number)

print(three(3))
print(first.three(3))
print(first.four(3))


#  Importing specific names from a module

#  from module_name import name1, name2, ...

#  Guess the random number

import random  # Import the random module

def number_guess(num):
    # Get a random number between 1-100
    target_number = random.randint(1, 100)
    
    # Compare parameter num to the random number
    if num < target_number:
        print(f"{num} is too low. Random number was {target_number}.")
    elif num > target_number:
        print(f"{num} is too high. Random number was {target_number}.")
    else:
        print(f"{num} is correct!")

if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo-random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)

#  Quadratic formula

import math  # Import math module

def quadratic_formula(a, b, c):
    # Compute the quadratic formula results in variables x1 and x2
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    else:
        raise ValueError("Discriminant is negative, quadratic equation has no real solutions.")

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print(f'{prefix_str}{number:.0f}')
    else:
        print(f'{prefix_str}{number:.2f}')

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])
    try:
        solution = quadratic_formula(a, b, c)
        print(f'Solutions to {a:.0f}x^2 + {b:.0f}x + {c:.0f} = 0')
        print_number(solution[0], 'x1 = ')
        print_number(solution[1], 'x2 = ')
    except ValueError as e:
        print(e)

#  time
import time
localtime = time.asctime( time.localtime(time.time()) )
print( "Local current time is:", localtime )
"""

#  Selecting randomized items from a list.
# from random import choices
# items = [12, 6, 4, 18, 3, 5, 16]
# selection = choices(items, k=2)
# print(selection)

# #  date
# import datetime
# print(datetime.date.today())
#  calculate future date
# span = datetime.timedelta(days=7)
# today = datetime.date.today()
# futuredate = today + span
# print("One week from now will be: {}".format(futuredate))

#  Calculate area of a circle.
# from math import pi, ceil
# from math import pi, ceil
# def calcArea(radius):
#         area = pi * (radius**2)
#         return ceil(area)
# print(calcArea(7))
# print(calcArea(3))
# import math
# print(help(math))
# import random
# help(random.choices)
