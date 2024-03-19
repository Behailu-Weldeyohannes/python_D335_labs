
#  ********* Chapter Two: Types ********
"""
#  ----------string-------------

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

user_number = int(input('Enter number to use as index: '))
print()

print(f'\nThe letter at index', user_number, 'of the alphabet is', alphabet[user_number])

#Program to calculate statistics from student test scores.
midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]
#Combine the scores into a single list
all_scores = midterm_scores + final_scores
# print(all_scores)
num_midterm_scores = len(midterm_scores)
num_final_score = len(final_scores)
# print(num_midterm_scores)
# print(num_final_score)
avg_midterm = sum(midterm_scores) / len(midterm_scores)
avg_finalterm = sum(final_scores) / len(final_scores)
# print(f"{avg_midterm:.2f}")
# print(f"{avg_finalterm:.2f}")
#Calculate the number of students that took the midterm but not the final
dropped_students = num_midterm_scores - num_final_score
print(dropped_students, ' students must have dropped the class.')
#  calculate the lowest and highest
lowest_final = min(final_scores)
highest_final = max(final_scores)
print(lowest_final, highest_final)

user_age = [9,6,7,8,3]
result = user_age.index(7)
# print(result)
add = sum(user_age)
print(add)

# ------------------list------------------
#  a mutable, ordered collection of elements. 
my_list = [1,2,3,4,'hello', 4.5]
print("list:", my_list)

# -------------- tuple-------------------
#  an immutable, ordered collection of elements

my_tuple = (1,2,3,"hello", 4.5)
# accessing elements
print("Tuple:", my_tuple)
# print("Tuple:", my_tuple[1])
#  tuple unpacking
a,b,c,d,e = my_tuple
print("Unpacked elements:", a,b,c,d,e)

#  iterating through a tuple
# print("Iterating through the tuple:")
# for item in my_tuple:
#     print(item)

#  ----------------set------------
#  an unordered, mutable collection of unique elements.
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Adding elements to a set
my_set.add(6)
my_set.update({7, 8, 9})
print("After adding elements:", my_set)
# Removing elements from a set
my_set.remove(3)
print("After removing 3:", my_set)

# Checking if an element is in the set
print("Is 5 in the set?", 5 in my_set)

# Iterating through a set
print("Iterating through the set:")
for element in my_set:
    print(element)

#  set operation 

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
#  union
union_set = set1 | set2
print(union_set)
#  intersection
intersection_set = set1 & set2
print(intersection_set)

# Difference of sets
difference_set = set1 -set2
print(difference_set)
# ------------ dictionary ---------------------
#  a mutable, unordered collection of key-value pairs.
#  creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# print("Dictionary:", my_dict)
# Accessing values using keys
# print("Name:", my_dict['name'])
# print("Age:", my_dict['age'])
# print("City:", my_dict['city'])
#  modifying values
my_dict['age'] = 26
# print("Updated age:", my_dict['age'])
#  adding a new-value pair
my_dict['gender'] = 'Male'
# print("Updated dictionary", my_dict)
# removing a key-value pair
del my_dict['city']
# print("Dictionary after removing city:", my_dict)

#  checking if the key is in the dict
# print('name' in my_dict)
#  iterating through dict
for key, value in my_dict.items():
    print(f"{key}: {value}")

#  grade calculator
exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))

overall_grade = (exam1_grade + exam2_grade + exam3_grade) / 3

print(f'Your overall or average grade is: {overall_grade:.1f}')
num_items = 5
item_weight = 0.5
result = (num_items + num_items) * item_weight
print(result)
#  f-string features
# print(f'{2 * 2=}')
kids = 4
adults = 2
output1 = f'{kids+adults=} total'
print(output1)
output = f'{{2}} + {{3}} = {{5}}'
print(output)
#  labs
# Health data
user_age_years = int(input('enter your age in years:\n'))

user_age_days = user_age_years  * 365
user_age_hours = user_age_years * user_age_days
user_age_minutes = user_age_hours * 60
user_age_seconds = user_age_minutes * 60
heart_beat_per_minute = user_age_minutes * 72


print(f'You are at least {user_age_days} days old.')
print(f'You are at least {user_age_hours:.0f} hours old.')
print(f'You are at least {user_age_minutes:.0f} minutes old.')
print(f'You are at least {user_age_seconds:.0f} seconds old.')

# Caffeine levels

caffeine_mg = float(input())

half_life_hours = 6
after_6 = caffeine_mg / 2
after_12 = after_6 / 2
after_24 = caffeine_mg / (2 ** 4) #  final_amount  = initial amount / (2 the power of num of half life periods )

print(f"After 6 hours: {after_6:.2f} mg")
print(f"After 12 hours: {after_12:.2f} mg")
print(f"After 24 hours: {after_24:.2f} mg")
#  House real estate summary
currrent_price = int(input())
last_month_price = int(input())
price_change = currrent_price - last_month_price
monthly_mortgage = (currrent_price * 0.051) / 12

print(f"This house is ${currrent_price}. The change is ${price_change} since last month.")
print(f"The estimated monthly mortgage is ${monthly_mortgage:.2f}.")
#  simple statistics
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

''' Type your code here. '''
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# Output as rounded integers
print(f'{product:.0f} {round(average):.0f}')

# Output as floating-point numbers with three digits after the decimal point
print(f'{product:.3f} {average:.3f}')
"""
