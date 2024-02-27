
#  ***********Types *******************

#  Creating passwords
# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
word1 = input()
word2 = input()
num = int(input())
print(f"You entered: {word1} {word2} {num}")
print()

# favorite_color = input('Enter favorite color:\n')


# FIXME (2): Output two password options
word2 = word2.capitalize()
password1 = f"{word1}_{word2}"
password2 = f"{num}{word1}{num}"
print(f"First password: {password1}")
print(f"Second password: {password2}")
# print('\nFirst password:')
print()


# FIXME (3): Output the length of the two password options
password1_len = len(password1)
password2_len = len(password2)
print(f"Number of characters in {password1}: {password1_len}")
print(f"Number of characters in {password2}: {password2_len}")


#  painting a wall
from math import ceil                     # needed in Step #3
# part 1
height = float(input())
width = float(input())
cost = float(input())
area = height * width
print(f"Wall area: {area:.1f} sq ft")
# print()
# part2
# One gallon of paint covers 350 square feet
gallon_needed = area / 350
print(f"Paint needed: {gallon_needed:.3f} gallons")
# part 3
cans_needed = ceil(gallon_needed)
print(f"Cans needed: {cans_needed} can(s)")

# part 4
paint_cost = cost * cans_needed
sales_tax = 0.07 * paint_cost
total_cost = paint_cost + sales_tax
print(f"Paint cost: ${paint_cost:.2f}\nSales tax: ${sales_tax:.2f}\nTotal cost: ${total_cost:.2f}")