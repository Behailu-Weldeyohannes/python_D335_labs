#  ************* Loops ****************
"""
#  Given a line of text as input, output the number of characters excluding spaces, periods, exclamation points, or commas.

text = input()
count = 0

for char in text:
    if char not in (' ', '.', '!', ','):
        count += 1
print(count)

#  Countdown until matching digits
# Read an integer in the range 11-100
num = int(input())

# Validate input range
if 11 <= num <= 100:
    # Output countdown until both digits are identical
    while num // 10 % 10 != num % 10:
        print(num)
        num -= 1

    # Print the final number where both digits are identical
    print(num)
else:
    print("Input must be 11-100")

#  Smallest and largest numbers in a list
# Initialize an empty list to store integers
integer_list = []

# Read integers until a non-positive integer is encountered
# Initialize an empty list to store integers
integer_list = []

# Read integers until a non-positive integer is encountered
while True:
    num = int(input())
    if num > 0:
        integer_list.append(num)
    else:
        break

# Output the smallest and largest integers
min_integer = min(integer_list)
max_integer = max(integer_list)

print(f'{min_integer} and {max_integer}')


#  Output values in a list below a user defined amount
#  for string
sco = "100  79  89  99  95"
student_scores = sco.split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"the highest score in the class is {highest_score}")

sco = [100, 101,79, 89, 99, 95]

highest_score = 0


for score in sco:
    if score > highest_score:
        highest_score = score
    
print(f"the highest score in the class is {highest_score}")

sco2 = [100, 101,79, 89, 99, 95]
# lowest_score =int(input())
lowest_score = sco2[0]

for score in sco2:
    if score < lowest_score:
        lowest_score = score

print(f"the highest score in the class is {lowest_score}")

#  find the oldest and the younest ages
score = [100, 102, 99, 89, 95]

highest_score = 0

for grade in score:
    if grade > highest_score:
        highest_score = grade
print(highest_score)


age = [100, 108, 45, 110, 67, 1, 0, 43, 10]

young = age[0]

for youngest in age:
    if youngest < young:
        young = youngest
# print(young)

senior = 0

for eldest in age:
    if eldest > senior:
        senior = eldest
print(senior)

#  range
# for num in range(1, 10):
    # print(num)

# for num2 in range(1, 20, 2):
#     print(num2)
#  add number from 1 to 100
# total = 0
# for num in range(1, 101):
#     total += num
# print(total)
#  add even numbers
user_num = int(input())  # num between 0 and 1000
even_sum = 0

for num in range(2, user_num + 1, 2):
    even_sum += num
print(even_sum)

#  or
user_num2 = int(input())
sum = 0

if user_num2 % 2 != 0:
    print("Please use an even number")
else:
    for num in range(1, user_num2 + 1):
        if num % 2 == 0:
            sum += num
    print(f" Sum of even number: {sum}")


user_num = int(input())

for num in range(1, user_num + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
      
#  Password generator project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the Password Generator")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

#  easy
# import random
# password = ""

# for char in range(1, num_letters + 1):
#     password += random.choice(letters)
# for symb in range(1, num_symbols + 1):
#     password += random.choice(symbols)
# for num in range(1, num_numbers + 1):
#     password += random.choice(numbers)
 
# print(password)  
# password = ""

#  hard way
import random

password_list = []
for char in range(1, num_letters + 1):
    # password_list += random.choice(letters)
    password_list.append(random.choice(letters))
for symb in range(1, num_symbols + 1):
    # password_list += random.choice(symbols)
    password_list.append(random.choice(symbols))
for num in range(1, num_numbers + 1):
    # password_list += random.choice(numbers)
    password_list.append(random.choice(numbers))
 
print(password_list) 
random.shuffle(password_list) 
# print(password_list)

my_password = ""
for password in password_list:
    my_password += password

print(f"Your password is: {my_password}")

int_list = int(input())
integer_list = []

for i in range(int_list):
    value = int(input())
    integer_list.append(value)

threshold = int(input())

for  num in integer_list:
    if num <= threshold:
        print(num, end="")
print()


low = int(input())
high = int(input())
x = int(input())
count = 0

for num in range(low, high + 1):
    if num % x == 0:
        count += 1
print(f"The number of multiplies of {x} between {low} and {high} inclusive is: {count}")
 
#  Using range() and len() to iterate over a sequence.
origins = [4, 8, 10]

# for index in range(len(origins)):
#     value = origins[index]
#     print(f"Element {index}: value")

#  Using list.index() to find the index of each element.
for num in origins:
    index = origins.index(num)
    print(f"Element {index}: {num}")


# my_string = " Just sit right back and we'll talk about Love and Nation."

# my_tuple = ("Peter", "Jemanesh", "Konjo","Naomi")
# my_dict = {"Peter": "random name", "Jemanesh": "Mother", "Konjo":"lover","Naomi": "doughter"}
#  **************loop and string *************
# for char_str in my_string:
    # print(char_str)
#  range()

# for i in range(len(my_string)):
#     ranged_str = my_string[i]
#     print(ranged_str)
#    split() 
# words = my_string.split()
# for word in words:
#     print(word)
# for word in words:
#     print(word)

#  using list comprehension with strings
# for char in [a for a in my_string]:
#     print(char)

#  enumerate for index and charcters
# for index, char in enumerate(my_string):
#     print(f"{index}, {char}")
#  combine split() and enumerate

# words_key = my_string.split()

# for key, word in enumerate(words_key):
#     print(f"{key}: {word}")


#  **********List and loop ***********
# my_list = ["Gilligan", "Behailu", "Mesi", "Peter", "Jill", 3]
#  using list comprehension
# my_sec_list = [1, 2,4,6,7,82,7,5]

# double_list = [item * 2 for item in my_sec_list]

# for item in double_list:
    # print(item)
# half_list = [item / 2 for item in my_sec_list]

# for num in half_list:
#     print(num)

# for lst in my_list:
#     print(lst)
# for lst in range(len(my_list)):
#     print(my_list[lst])
# for index, lst in enumerate(my_list):
#     print(f"{index}: {lst}")
#   using zip to loop over multiple lists
# my_list = ["Gilligan", "Behailu", "Mesi", "Peter", "Jill", 3]
# my_second_list = [1,2,3,4,5,6,"Yes"]
# for item1, item2 in zip(my_list, my_second_list):
#     print(f"Item from list1: {item1}, Item from list2: {item2}")


# my_tuple = ("Peter", "Jemanesh", "Konjo","Naomi")

# for tuples in my_tuple:
#     print(tuples)

# for index, item in enumerate(my_tuple):
#     print(f"{index}: {item}")
#  tuple unpacking
# a,b,c,d = my_tuple
# print(f"{a} and {b}")

#  for index position: use enumerate()

# for index, item in enumerate(my_list):
#     print(f"{item} is at position {index}")
#  for numbers use range

# for num in range(0,5):
#     print("Hello")
#  * operator
# repeated_tuple = my_tuple * 3
# print(repeated_tuple)

# my_dict = {"Peter": "random name", "Jemanesh": "Mother", "Konjo":"lover","Naomi": "doughter"}
# for key in my_dict:
#      value = dict[key]
#      print(f"{key} is my {my_dict[key]}")
# for key in my_dict:
#     print(f"{key}: {my_dict[key]}")
# for key in my_dict:
#     value = my_dict[key]
#     print(f"{key}: {value}")

# for key, value in my_dict.items():
#     print("{} is a {}".format(key, value))

#  nested loop
low = int(input())
high = int(input())
x = int(input())
multiplies = 0

for num in range(low, high + 1):
    if num % x ==0:
        multiplies+= 1
print(multiplies)


#  Hailstone sequence
input = int(input())
count = 0
while input != 1:
    print(input, end='\t')

    if input % 2 == 0:
        input //= 2
    else: 
        input = 3 * input + 1
    count +=1
    if count % 10 == 0:
        print()
print(1, end='\t')
    

low = int(input())
high = int(input())
x = int(input())
num_of_multiply = 0

for num in range(low, high + 1):
    if num % x == 0:
        num_of_multiply = num_of_multiply + 1
print(num_of_multiply)

#  find the largest num

largest = 0
while True:
    int_num = int(input())
    if int_num < 0:
        break
    if int_num > largest:
        largest = int_num
print(largest)


#  read input
num = int(input())
count = 0

#  process and print the hailstone sequence
while num != 1:
    print(num, end='\t')
    if num % 2 == 0:
        num = num // 2
    else:
        num = 3 * num + 1
    count += 1
# print new line every 10 number
    if count % 10 == 0:
        print()
#  print the last number(1)
print (num)


#  numbers in reverse

int_list = []

while True:
    num = input()
    if num == "*":
        break
    int_list.append(int(num))

while int_list:
    print(int_list.pop(), end='')
    if int_list:
        print(",", end="")
print()

 
#  Output values in a list below a user defined amount
num_int = int(input())
# print(f"I'm the first integer{num_int}")

int_list = [int(input()) for num in range(num_int)]

print(f"I am the second{int_list}")

threshold = int(input())
print(f"I am threshold{threshold}")

output = [str(num) +"," for num in int_list if num <= threshold]
print(f"I am output {output}")

print("".join(output))

integer_list = [int(input()) for _ in range(num_int)]

print(integer_list)

first_int = int(input())
# first_int = 5

int_list = [int(input()) for num in range(first_int)]
print(int_list)
threshold = int(input())
print(threshold)

less_threshold = [str(num) + "," for num in int_list if num < threshold]
print(less_threshold)
print("".join(less_threshold))

#  Draw upside down triangle
height = int(input())

for i in range(height, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
#  Draw right-justified triangle
# Get user input for the height
height = int(input())

height = int(input())
for i in range(1, height + 1):
    total_space = height - i
    print(" " * total_space, end="")
    print("* " * i)

#   Matching strings
str_a = input()
str_b = input()

count = 0

for c1, c2 in zip(str_a, str_b):
    if c1 == c2:
        count = count + 1

if count == 1:
    print(f"{count} character matches")
else:
    print(f"{count} characters match")

#  Months until payoff
loan_amount = float(input())
payment_amount = float(input())
interest_rate = float(input())

current_balance = loan_amount
num_payments = 0

while current_balance > 0:
    current_balance = current_balance * (1 + interest_rate)
    current_balance = current_balance - payment_amount
    num_payments = num_payments + 1

if num_payments > 1:
    print(f"{num_payments:.1f} payments")
else:
    print(f"{num_payments:.1f} payment")
    """









  




