
#  ********* Chapter Four: Loops ********
"""

#  ------ counting------------

limit = int(input())

# for i in range(1, limit + 1):
#     print(i)

for j in range(limit, -1,-2): # start, stop, step  
    print(j)
x = 3 # 
while x >= 1: # First check, x is 3, so x >= 1 is True., Second check, x is 2, still True., Third check, x is 1, still True., Fourth check, x is 0, so x >= 1 is False.
    x = x -1 #
print(x) #
user_char = input()
while user_char !='n':
    print(f"{user_char}")

nose = '0'  # Looks a little like a nose
user_value = '-'

while user_value != 'q':
    print(f' {user_value} {user_value} ')  # Print eyes     
    print(f'  {nose}  ')  # Print nose     
    print(user_value*5)  # Print mouth
    print('\n')

    # Get new character for eyes and mouth
    user_input = input("Enter a character ('q' for quit): \n")
    user_value = user_input[0]

print('Goodbye.\n')

#  -----------While loop: Iterations---------

year_considered = 2024  # Year being considered
num_ancestors = 2  # Approx. ancestors in considered year
years_per_generation = 20  # Approx. years per generation

user_year = int(input('Enter a past year (neg. for B.C.): '))
print()

while year_considered >= user_year:
    print(f'Ancestors in {year_considered}: {num_ancestors}')
    
    num_ancestors = num_ancestors * 2
    year_considered = year_considered - years_per_generation

x = 1
y = 3
z = 5
while not (y < x < z):
    print(x, end=' ')
    x = x + 1

g = 0

while g <= 4:
    print(g)
    g += 2
g = 0

while g >= -3:
    print(g)
    g -= 1

g = 0

while g >= -6:
    print(g)
    g -= 4

g = 4

while g <= 5:
    print(g)
    g += 1


user_num = int(input())
while user_num >= 1:
    user_num = user_num / 2
    print(user_num)
# the greatest common divisor
num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_b
    else:
        num_b = num_b - num_a
print(f'GCD is {num_a}')
"""
#  conversion
'''
Program that has a conversation with the user.
Uses elif branching and a random number to mix up the program's responses.
import random  # Import a library to generate random numbers

print('Tell me something about yourself.')
print('You can type \'Goodbye\' at anytime to quit.\n')

user_text = input()

while user_text != 'Goodbye':
    random_num = random.randint(0, 2)  # Gives a random integer between 0 and 2
    if random_num == 0:
        print('\nPlease explain further.\n')
    elif random_num == 1:
        print(f"\nWhy do you say: '{user_text}'?\n")
    elif random_num == 2:
        print('\nWhat else can you share?\n')
    else:
        print('\nUh-oh, something went wrong. Try again.\n')

    user_text = input()

print('It was nice talking with you. Goodbye.\n')


'''
#  A sentinel value is used to terminate a loop's processing
'''
Outputs average of list of positive integers
List ends with 0 (sentinel)
Ex: 10 1 6 3 0  yields (10 + 1 + 6 + 3) / 4, or 5

values_sum = 0
num_values = 0

curr_value = int(input())
   
while curr_value > 0: # Get values until 0 (or less)
    values_sum += curr_value
    num_values += 1
    curr_value = int(input())

print(f'Average: {values_sum / num_values:.0f}\n')
#  max value
entered_value = int(input())
max_value = entered_value
while entered_value > 0:
    if entered_value > max_value:
        max_value = entered_value
    entered_value = int(input())
print('Max value:', max_value, end="")


#  min value

user_value = int(input())
min_num = user_value

while user_value > 0:
    if user_value < min_num:
        min_num = user_value
    user_value = int(input())
print("Min value", min_num, end="")
#  Bidding example.
import random
random.seed(5)

keep_bidding = 'y'
next_bid = 0

while keep_bidding == 'y':
# while keep_bidding == 'y':
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()

#   Insect growth.
num_insects = int(input()) # Must be >= 1


while num_insects >=1 and num_insects <= 100:
    print(num_insects, end=' ')
    num_insects = num_insects * 2

#  counting with while loop
#  outputs the amount of money in a savings account each year for the user-entered number of years, with $10,000 initial savings and 5% yearly interest:
initial_savings = 10000
interest_rate = 0.05

print(f'Initial savings of ${initial_savings}')
print(f'at {interest_rate*100:.0f}% yearly interest.\n')

years = int(input('Enter years: '))
print()
savings = initial_savings
i = 1
while i <= years:
    print(f"Savings at beginning of year {i}: ${savings:.2f}")
    savings = savings + (savings * interest_rate)
    i = i + 1
# Loop iterates 10 times.
j = 0

while j <= 10:
    j += 1
    print(j)
#  counting down with while loop
i = 5
while i >= 1:
    i -= 1
    print(i)

i = 10
while i >= 1:
    i -= 2
    print(i)
#  presidential election year
current_year = int(input("Enter the current year: "))
election_year = 1788

while election_year <= current_year:
    print(f'Election Year: {election_year}')
    election_year += 4

year = int(input("Enter the year to check: "))
election_year = 1788

if (year - election_year) % 4 == 0:
    print(f"{year} is an election year")
else:
    print(f"{year} is not an election year")
#  factorial
N = int(input())  # Read user-entered number
total = 1  # Initialize the total variable to 1

# Use a loop variable i that counts from N down to 1
i = N

while i > 0:
    total *= i  # Multiply total by i
    i -= 1      # Decrement i

print(f"{N}:{total}")

#  -----------for loop ---------

#  assigns the loop variable with a dictionary's keys
channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}
for c in channels:
    print(f"{c} is on channel {channels[c]}")
#  Calculating shop revenue
daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]

total = 0

for day in daily_revenues:
    total = total + day
    average = total / len(daily_revenues)

print(f"Weekly revenue: ${total:.2f}")
print(f"Daily average revenue: ${average:.2f}")

#  iterate backwards using reversed()
names = [
    'Biffle',
    'Bowyer', 
    'Busch',
    'Gordon',
    'Patrick'
]

# for name in names:
#     print(name, '|', end=" ")
#     print('\nPrinting in reverse:')
#     for name in reversed(names):
#         print(name, '|', end=" ")
for name in names:
    print(name)
    print("*********")
    for name in reversed(names):
        print(name)

#  calculate total and average
num_kids = [1, 1, 2, 2, 1, 4, 3, 1]
total = 0

for kids in num_kids:
    total = total + kids
    avearge = total / len(num_kids)
print(f"Total: {total}\nAverage:{avearge}")

temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
num_neg = 0
for temp in temperatures:
    if temp < 0:
        num_neg += 1
        print(f"Temprature: {temp}")
#  order from highest to lowest
scores = [75, 77, 80, 85, 90, 95, 99]

for score in reversed(scores):
    print(score, end="-")
weights = [1, 8, 2]
result = 0
for weight in weights:
    result -= weight
print(result)
# numbers = [4,8,3,1]
# # for num in numbers:
# for num in reversed(numbers):
#     # print("Num",num, end="")
#     print(num, end=" ")

numbers = [1,2,3,4,5]
sum = 0
for num in numbers:
    sum = sum + num
    avg = sum / len(numbers)
print(sum, avg, end="")

cities = {
    'London': 5259,
    'Rome': 958,
    'Nairobi': 550,
}
best = ""
distance = 0

for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)
#  print each price in stock_prices.
stock_prices = [input(), input(), input()]
for price in stock_prices:
    print(f"${price}")
#  output each contact in contact_emails
contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}
new_contact = input()
new_email = input()
# contact_emails [new_contact] = new_email
contact_emails[new_contact] = new_email

for contact, email in contact_emails.items():
    print(f"{email} is {contact}")

#  ----------range()---
#  The range() function can take up to three integer arguments.
#  range(y) non negative range(3) - 0,1,2
#  range(x,y) sequence of all integers range(-1, 3) -1,0,1,2
# range(x,y,z) z increament y

initial_savings = 10000
interest_rate = 0.05
years = int(input())
print()
savings = initial_savings
for i in range(years):
    print(f' Savings in year {i}: ${savings:.2f}')
    savings = savings + (savings*interest_rate)

print('\n')

#  ---- Nested loop---

print("Two-letter domain names:")

letter1 = 'a'
letter2 = '?'

while letter1 <='z':
    letter2 = 'a'
    while letter2 <= 'z':
        print(f"{letter1}{letter2}.com")
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

#  Histogram.

num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(num):
            print('*', end=' ')
        print('\n')

print('Goodbye.')
# 
for i in range(5):
    for j in range(10,12):
        print(f"{i}{j}")
c1 = 'a'
while c1 < 'b':
    c2 = 'a'
    while c2 <= 'c':
        print(f'{c1}{c2}', end = ' ')
        c2 = chr(ord(c2) + 1)
    c1 = chr(ord(c1) + 1)
i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print(f'{i1}{i2}', end=' ')
        i2 = i2 + 3
    i1 = i1 + 10
# count = 0
# for i in range(1):
#     for j in range(3):
#         count = count + 1
# print(count)
count = 0
for i in range(1):
    for j in range(2):
        count += 1
print(count)
i = 0
count = 0
while i < 3:
    for j in range(4):
        count = count + 1
    i = i + 1
print(count)
letter1 = 'h'
while letter1 < 'j':
    letter2 = 't'
    while letter2 <= 'v':
        print(f'{letter1}{letter2}')
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

i = 3
while i < 15:
    j = 5
    while j <= 9:
        print(f'{i}{j}')
        j = j + 4
    i = i + 19
#  rectangle with nestted loop

num_rows = int(input())
num_cols = int(input())

for i in range(num_rows):
    for j in range(num_cols):
        print('*', end=" ")
    print()

#  print seats
num_rows = int(input())
num_cols = int(input())
# Loop through rows and columns to print all seats
for i in range(1, num_rows + 1):
    for j in range(num_cols):
        seat = f"{i}{chr(65 + j)}"
        print(seat, end=' ')
print()

user_input = input('Enter phone number:\n')
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-') or (character == '+'):
        phone_number += character
    elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
        phone_number += '2'
    elif ('d' <= character <= 'f') or ('D' <= character <= 'F'):
        phone_number += '3'
    elif ('g' <= character <= 'i') or ('G' <= character <= 'I'):
        phone_number += '4'
    elif ('j' <= character <= 'l') or ('J' <= character <= 'L'):
        phone_number += '5'
    elif ('m' <= character <= 'o') or ('M' <= character <= 'O'):
        phone_number += '6'
    elif ('p' <= character <= 's') or ('P' <= character <= 'S'):
        phone_number += '7'
    elif ('t' <= character <= 'v') or ('T' <= character <= 'V'):
        phone_number += '8'
    elif ('w' <= character <= 'z') or ('W' <= character <= 'Z'):
        phone_number += '9'
    else:
        phone_number += '?'

print(f'Numbers only: {phone_number}')

#  break and continue
empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print(f'${meal_cost} buys {num_empanadas} empanadas and {num_tacos} tacos without change.')
else:
    print('You cannot buy a meal without having change left over.')


#  continue

for i in range(5):
    if i < 10:
        continue
    # print(i)
print(i)

stop = int(input())
for n in range(10):
    if n > stop:
        break
    print(n)

result = 0

for n in range(6):
    result = n - 2
    
    if (result % 2) != 0:
        print('_', end=' ')
        continue
    
    print(result, end=' ')

print('done')

a = int(input())
b = int(input())
c = int(input())
while a < b:
    print(a)

    if a > c:
        break
    a += 3
stop = int(input())
for a in range(5):
    result = 0
    for b in range(4):
        result += a * b
    print(result)
    if result > stop:
        break

stop = int(input())
result = 0

for a in range(3):
    print(a + 1, end=': ')
    
    for b in range(4):
        result += a + 1
        
        if result > stop:
            print('_', end=' ')
            continue
        
        print(result, end=' ')
    
    print()

#  Simon says
user_score = 0
simon_pattern = input("Simon's pattern: ")
user_pattern = input("Your pattern: ")

for simon_char, user_char in zip(simon_pattern, user_pattern):
    if simon_char == user_char:
        user_score += 1
    else:
        break

print('User score:', user_score)

# loop else
names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']
num = int(input('Enter number of names to print: '))
for i in range(len(names)):
    if i == num:
        break
    print(names[i], end=' ')
else:
    print("All names printed.")

#  baby names
#A few legal, acceptable Danish names
legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn', 
    'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne', 
    'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia', 
    'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne', 
    'Dorte'
]
user_name = input()
if user_name in legal_names:
    print(f'{user_name} is an acceptable Danish name. Congratulations.')
else:
    print(f'{user_name} is not acceptable.')
    for name in legal_names:
        if user_name[0] == name[0]:
            print(f'You might consider: {name},', end=' ')
            break
    else:
        print('No close matches were found.')
print('Goodbye.')

#  Getting both index and value when looping: enumerate()
#  enumerate()

#  option 1
origins = [4,8,10]
for index in range(len(origins)):
    value = origins[index]
    print(f'Element{index}: value')
#  option 2
origins = [4,8,10]
for value in origins:
    index = origins.index(value) # Retrieve index of value in list
    print(f'Element {index}: {value}')
#  option 3
origins = [4,8,10]
for (index, value) in enumerate(origins):
    print(f'Element {index}: {value}')
# my_list = [2,3,4,6]
my_list = ['Greek', 'Nordic', 'Mayan']
for (index, value) in enumerate(my_list):
    print(index, value)
#  Dice statistics
#  calculates the number of times the sum of two dice (randomly rolled) is equal to six or seven.
import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print(f'Roll {i} is {roll_total} ({die1} + {die2})')

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')


#  convert to reverse binary

num = int(input())
result = ''

while num > 0:
    result = result + str(num % 2)
    num = num // 2
print(result)
#  option 2
num2 = int(input())
binary_str = format(num2, 'b')[::-1]
print(binary_str)
#  get the binary
# num = 10
# binary_str = format(num, 'b')
# print(binary_str)

number = int(input())
binary_num = format(number, 'b')
print(binary_num)
print("*******")
#  get the reverse binary
num2 = int(input())
reverse_binary = format(num2, 'b')[::-1]
print(reverse_binary)

# Password modifier
# Get input password from the user
password = input("Enter a simple password: ")

# Apply replacements and build the stronger password
stronger_password = ""
for char in password:
    if char == 'i':
        stronger_password += '1'
    elif char == 'a':
        stronger_password += '@'
    elif char == 'm':
        stronger_password += 'M'
    elif char == 'B':
        stronger_password += '8'
    elif char == 's':
        stronger_password += '$'
    else:
        stronger_password += char

# Append '!' to the end of the stronger password
stronger_password += '!'

# Output the stronger password
print("Stronger Password:", stronger_password)


# Brute force equation solver
#   use brute force to find an integer solution for x and y in the range -10 to 10.
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

found_solution = False
for x in range(-10,10):
    for y in range(-10,10):
        if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
            print(f"x= {x}, y= {y}")
            found_solution = True
            break
    if found_solution:
        break
if not found_solution:
    print("There is no solution")

#  Adjust values in a list by normalizing
num_values = int(input())
values = []

for _ in range(num_values):
    value = float(input())
    values.append(value)
max_value = max(values)

for value in values:
    adjusted_value = value / max_value
    print(f"{adjusted_value:.2f}")
'''
