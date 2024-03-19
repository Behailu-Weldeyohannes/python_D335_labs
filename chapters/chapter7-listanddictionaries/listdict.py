
#  ********* Chapter Seven: Lists and Dictionaries ********
"""


#  --------Lists---------

my_list = ['hello', -2, 4.5, 6]

oldest_people = [122, 119, 117, 117, 116] 

nth_person = int(input('Enter N (1-5): '))
if (nth_person >= 1) and (nth_person <= 5):
    print(f"{nth_person}th oldest person lived {oldest_people[nth_person-1]} years")
my_list = list('123')
print(my_list)

my_list = [1, 2] + [3] 
print(my_list)

my_list = [1, 2, 3]
my_list[len(my_list):] = [9]
print(my_list)
my_list = [1, 2, 3]
del my_list[1]
print(my_list)

user_values = [3, 6, 9]
user_values[0] = user_values[0] + 1

print(user_values)

user_values = [1, 4, 8]
user_values[0] = user_values[1]

print(user_values)
user_input = input()
short_names = user_input.split()

del short_names[0]
short_names[-1] = 'Joe'


print(short_names)

#  list methods

# --------------------add elements-----------------
# list.append(x)

my_list = [5, 8]
my_list.append(16)
print(my_list)

# list.extend([x])
my_list = [5, 8]
my_list.extend([4, 12])
print(my_list)

#  list.insert(i,x)
my_list = [5, 8]
my_list.insert(1, 1.7)
print(my_list)

#  ---------------------removing elements--------------
# list.remove(x)
my_list = [5,8,14]
my_list.remove(8)
print(my_list)

# list.pop()
my_list2 = [5, 8, 14]
# val = my_list2.pop()
val2 = my_list2.pop(1)
print(val2)
print(my_list2)

#  ------------- Modifying elements ---------------
# list.sort()
my_list = [14, 5, 8]
my_list.sort()
print(my_list)
#  list.reverse()

my_list = [14, 5, 8]
my_list.sort()
my_list.reverse()
print(my_list)

#  Miscellaneous
# list.index(x)
my_list = [5, 8, 14]
print(my_list.index(14))

# list.count(x)
my_list = [5, 8, 5, 5, 14]
print(my_list.count(5))
# print(my_list)
user_input = input()
short_names = user_input.split()
short_names.sort()
short_names.reverse()
print(short_names)

#  List iteration

nums = [1, 4, 15, 456]

# max_even = None
# for num in nums:
#     if num % 2 == 0:
#         if max_even == None or num > max_even:
#             max_even = num
# print(num)

    # print(num)
even_num = [num for num in nums if num % 2 == 0]
max_even = max(even_num)

print(max_even)
num = [3,6,7,9,3,1,9,5]

cnt_odd = 0

# odd = [n for n in num if n % 2 ==1]
# cnt_odd = cnt_odd + len(odd)
# print(cnt_odd)

for n in num:
    if n % 2 == 1:
        cnt_odd = cnt_odd + 1
print(cnt_odd)
inp = input().split()
cnt_neg = 0

neg_num = []

num = input()
div_ten = 0
num_div = [i for i in num if i % 10 ==0]
div_ten += len(num_div)
print(div_ten)

for i in num:
    if i % 10 == 0:
        div_ten += 1
    print(div_ten) 

# IndexError and enumerate()

user_input = input('Enter numbers: ')
tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print(f'{pos}: {token}')

sum = 0
for num in nums:
    sum += num

print('Sum:', sum)
# print(all([1, 2, 3]))
# print(all([0, 1, 2]))
print(max([-3, 5, 25]))
print(min([-3, 5, 25]))
print(sum([-3, 5, 25]))
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]
total_points = sum(points)
avg_ppg = total_points / sum(games_played)
#  best scoring year
max_points = max(points)
best_year_index = points.index(max_points)
best_year = 2003 + best_year_index
#  worest scoring year

min_points = min(points)
worst_year_index = points.index(min_points)
worst_year = 2003 + worst_year_index

# Print the statistics
print("Total career points:", total_points)
print("Average points per game:", avg_ppg)
print("Best scoring year:", best_year)
print("Worst scoring year:", worst_year)

my_list = [0, 5, 10, 15]
print(any(my_list))
print(all(my_list))
num_guesses = int(input())
user_guesses = [int(input("".format(i + 1))) for i in range(num_guesses)]
print('user_guesses:', user_guesses)
#  or
num_guesses = int(input())
user_guesses = []

for i in range(num_guesses):
    guess = int(input("".format(i + 1)))
    user_guesses.append(guess)

print('user_guesses:', user_guesses)

# Sum extra credit.
user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


sum_extra = 0 # Initialize 0 before your loop

for grade in test_grades:
    if grade > 100:
        extra_credit = grade - 100
        sum_extra += extra_credit

print('Sum extra:', sum_extra)
user_input = input()
hourly_temperature = user_input.split()

for index, temp in enumerate(hourly_temperature):
    if index < len(hourly_temperature) -1:
        print(f"{temp} -> ", end="")
    else:
        print(f"{temp}", end=" \n")
#  List nesting
my_list = [[10, 20], [30, 40]]
print(my_list[0])
print(my_list[0][0])
#  a tic-tac-toe board
tic_tac_toe = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', 'O', 'X']
]

print(tic_tac_toe[0][0], tic_tac_toe[0][1], tic_tac_toe[0][2])
print(tic_tac_toe[1][0], tic_tac_toe[1][1], tic_tac_toe[1][2])
print(tic_tac_toe[2][0], tic_tac_toe[2][1], tic_tac_toe[2][2])
#  Driving distance between cities.
# direct driving distances between cities, in miles
# 0: Boston    1: Chicago    2: Los Angeles

distances = [
    [
        0,  
        960,  # Boston-Chicago
        2960 # Boston-Los Angeles
    ],
    [
        960,  # Chicago-Boston
        0,
        2011  # Chicago-Los Angeles
    ],
    [
        2960,  # Los Angeles-Boston
        2011,  # Los Angeles-Chicago
        0
    ]
]
user_input = input('Enter city pair (Ex: 1 2) -- ').strip()
city1, city2 = user_input.split()

print(f'Distance: {distances[int(city1)][int(city2)]} miles')


currency = [
    
        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]
for row in currency:
    for cell in row:
        print(cell, end=" ")
    print()

currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
    for column_index, item in enumerate(row):
        print(f'currency[{row_index}][{column_index}] is {item:.2f}')

#  Print the two-dimensional list mult_table by row and column
user_input = input("Enter the two-dimensional list separated by commas: ")
lines = user_input.split(',')

# Convert the input string into a two-dimensional list
mult_table = [[int(num) for num in line.split()] for line in lines]

# Print the two-dimensional list by row and column
for row in mult_table:
    for col in row:
        print(col, end=" | ")  # Separate elements with a pipe character
    print()  # Move to the next line for the next row
#  List slicing
boston_bruins = ['Tyler', 'Zdeno', 'Patrice']
print('Elements 0 and 1:', boston_bruins[0:3])
print('Elements 0 and 1:', boston_bruins[1:3])
my_list = ['practicing', 'with', 'list', 'slicing']
print(my_list[0:4])
election_years = [1992, 1996, 2000, 2004, 2008]
print(election_years[0:-1])
print(election_years[-3:-1])
print(election_years[0:2])
nums = [0, 25, 50, 75, 100]
print(nums[0:5:2])
print(nums[0:-1:3])
my_list = [5, 10, 20]
print(my_list[0:2])

my_list = [5, 10, 20, 40, 80]
print(my_list[0:5:3])

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
prin = my_list[len(my_list) // 2:(len(my_list)//2) + 1]
print(prin)

# Loops modifying lists
my_list = [3.2, 5.0, 16.5, 12.25]
for i in range(len(my_list)):
    my_list[i] += 5
print(my_list)
nums = [50, 10, -5, -4, 6]
for n in range(len(nums)):
    if nums[n] < 0:
        nums[n]= 0
print(nums)
user_values = [2, 5, 9]
for i in range(len(user_values)):
    print(user_values[i])
user_values = [3, 4, 8]
sum_value = 0
for pos in range(len(user_values)):
    sum_value += user_values[pos]
print(sum_value)

user_values = [-1, 4, 6, -8]
for i in range(len(user_values)):
    if user_values[i] < 0:
        print(user_values[i])
user_values = [-1, 3, -5, 7]
for n in range(len(user_values)):
    if user_values[n] < 0:
        user_values[n] = -1 * user_values[n]
    print(user_values[n])
user_values = [1, 6, 8, 4]
max_value = user_values[0]
for i in range(len(user_values)):
    if user_values[i] >= max_value:
        max_value = user_values[i]
        print(max_value)
nums = [10, 20, 30, 40, 50]

for pos in range(len(nums)):
    tmp = nums[pos] / 2
    if (tmp % 2) == 0:
        nums[pos] = tmp
print(nums[1])
#  List comprehensions

my_list = [10, 20, 30]
list_plus = [(i + 5) for i in my_list]
print(list_plus)
#  using list comprehension
my_list = [5,10,50]
my_list = [(i + 5) for i in my_list]
print(my_list)
#  using for loop

my_list = [5,20,50]

for i in range(len(my_list)):
    my_list[i] = my_list[i] + 10
print(my_list)

list_plus = [(i + 10) for i in my_list]
print(list_plus)
#  convert to a string

my_list = [5, 20, 50]
my_list = [str(i) for i in my_list]
print(my_list)

for i in range(len(my_list)):
    my_list[i] = str(my_list[i])
#  convert user input to list of integers
inp = input()
my_list = [int(i) for i in inp.split()]
print(my_list)

my_list = []
for i in inp.split():
    my_list.append(int(i))
print(my_list)
#  Find the sum of each row in a two-dimensional list.
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = [sum(row) for row in my_list]
print(sum_list)

sum_list = []
for row in my_list:
    sum_list.append(sum(row))
print(sum_list)
my_list = [[5, 10, 15], [2, 3, 16], [100]]
min_row = min([sum(row) for row in my_list])
print(min_row)

my_list = [-5, -4, -3]
my_list = [x **2 for x in my_list]
print(my_list)
my_list = [5, 20, 50]

my_list = [float(i) for i in my_list]
print(my_list)
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = sum([sum(row) for row in my_list])
print(sum_list)
#  The largest square root of any element in x
x = [3,4]
squaree = max(math.sqrt(abs(num)) for num in x)
print(squaree)

# Conditional list comprehensions
#  a list of int from a user
numbers = [int(i) for i in input().split()]
odd_num = [odd for odd in numbers if (odd % 2 == 1)]
print(odd_num)

#  only negative values in the list x

neg = [i for i in input().split() if i < 0]
#  Only negative odd values from the list x

odd_neg = [i for i in input().split() if (i <0) and (i % 2) == 1]
my_list = [-1, 0, 1, 2]

new_list = [number * 5 for number in my_list]
print(new_list)

my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [number for number in my_list if number <= -1]
print(new_list)
my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [(number + 5) for number in my_list if number <= -2]
print(new_list)

my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [(number -3) for number in my_list if (number < -2) and (number % 2 == 1)]
print(new_list)
#  Sorting lists
#  Alphabetically sorting book titles
books = []
prompt = 'Enter new book: '
user_input = input(prompt).strip()

while (user_input.lower() != 'exit'):
    books.append(user_input)
    user_input = input(prompt).strip()

books.sort()

print('\nAlphabetical order:')
for book in books:
    print(book)
# numbers = [int(i) for i in input('Enter numbers: ').split()]

numbers = [int(i) for i in input("Enter number").split()]

sorted_numbers = sorted(numbers)

print('\nOriginal numbers:', numbers)
print('Sorted numbers:', sorted_numbers)
my_list = [[25], [15, 25, 35], [10, 15]]
my_list.sort()
print(my_list)
sorted_list = sorted(my_list, key=max)

print('Sorted list:', sorted_list)

#  ------- Dictionaries ------------- contain references to objects as key-value pairs 


student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        student_grades[name] = grade
        print(f"Grade for {name} updated to {grade}")
    elif command == '2':
        if name in student_grades:
            del student_grades[name]
            print(f"Grade for {name} deleted.")
        else:
            print(f"No grade found for {name}.")

    elif command == '3':
        print("Student Grades")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    elif command == '4':
        break
    else:
        print('Unrecognized command.')

#  Delete Prussia from country_capital.

airport_codes = {}
airport_codes['Washington'] = 'IAD'
airport_codes['Atlanta'] = 'ATL'
airport_codes['Vancouver'] = 'YVR'
print(airport_codes['Atlanta'])
print(airport_codes['Atlanta'])
print(airport_codes['Washington'])

# Dictionary methods

#  clear()
my_dict = {'Ahmad': 1, 'Jane': 42}
my_dict.clear()
print(my_dict)

# my_dict.get(key, default)

my_dict = {'Ahmad': 1, 'Jane': 42}
print(my_dict.get('Jane', 'N/A'))
print(my_dict.get('Chad', 'Cool'))
#  my_dict1.update(my_dict2)
my_dict1 = {'Peter': 1, "Sweet": 2}
my_dict1.update({'Flex': 4})
print(my_dict1)

my_dict2 = {"Konjo": 5, "Mesti": 6, "Soli": 7}
my_dict1.update(my_dict2)
print(my_dict1)
# my_dict.pop(key, default)
my_dict = {'Ahmad': 1, 'Jane': 42}
val = my_dict.pop('Ahmad')
print(my_dict)
print(val)

airport_codes = {
    'San Francisco': 'SFO',
    'Dallas': 'DAL',
    'New York': 'JFK',
    'Austin': 'AUS',
    'Chicago': 'ORD'
}

print(airport_codes.get('San Francisco', 'na'))
print(airport_codes.get('Vancouver', 'na'))
print(airport_codes.get('Amsterdam', 'na'))
airport_codes = {
    'Chicago': 'ORD',
    'Vancouver': 'YVR',
    'Austin': 'AUS',
    'Cincinnati': 'CVG',
    'Seattle': 'SEA'
}

print(airport_codes.get('Austin', 'na'))
print(airport_codes.pop('Austin', 'na'))
print(airport_codes.get('Austin', 'na'))
airport_codes = {
    'Vancouver': 'YVR',
    'Amsterdam': 'AMS',
    'London': 'LHR',
    'San Jose': 'SJC',
    'Paris': 'CDG'
}

new_airport_codes = {
    'Cincinnati': 'CVG',
    'Atlanta': 'ATL',
    'Houston': 'IAH'
}

print(airport_codes.get('Cincinnati', 'na'))
print(airport_codes.get('Dallas', 'na'))
print(airport_codes.get('Vancouver', 'na'))
airport_codes.update(new_airport_codes)
print(airport_codes.get('Cincinnati', 'na'))
print(airport_codes.get('Dallas', 'na'))
print(airport_codes.get('Vancouver', 'na'))


airport_codes = {
    'Paris': 'CDG',
    'Washington': 'IAD',
    'Cincinnati': 'CVG',
    'San Jose': 'SJC',
    'London': 'LHR'
}

new_airport_codes = {
    'London': 'LCY',
    'Minneapolis': 'MSP',
    'San Francisco': 'SFO'
}

print(airport_codes.get('London', 'na'))
print(airport_codes.get('Minneapolis', 'na'))
airport_codes.update(new_airport_codes)
print(airport_codes.get('London', 'na'))
print(airport_codes.get('Minneapolis', 'na'))

#  -----  Iterating over a dictionary -----
#  dict.items()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda, calor in num_calories.items():
    print(f"{soda}: {calor}", end="")
#  dict.keys()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.keys():
    print(soda)
#  dict.values()
for calor in num_calories.values():
    print(calor)
solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list

sorted_distance_list = sorted(list_of_distances)
closest = sorted_distance_list[0]
next_closest = sorted_distance_list[1]

print(f'Closest planet is {closest:.4e}')
print(f'Second closest planet is {next_closest:.4e}')
# Print the name and grade percentage of the student with the highest total of points.
# Find the average score of each assignment.
# Find and apply a curve to each student's total score, such that the best student has 100% of the total points.
#  use keys(), values(), and/or items() dict methods
# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99],
    'Example':[15, 19, 15, 20, 17]
}

user_input = input()
entries = user_input.split(',')
country_pop = {}

for pair in entries:
    split_pair = pair.split(':')
    country_pop[split_pair[0]] = split_pair[1]
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }

for country, pop in country_pop.items():

    print(f'{country} has {pop} people.')

#  Dictionary nesting
students = {}
students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}
print('Jose')

#  Varied amount of input data

user_num = input()
number = [int(num) for num in user_num.split()]
avg = round(sum(number) / len(number))
max = max(number)
print(f"{avg} {max}")
#  Filter and sort a list

user_input = input()
number = [int(num) for num in user_input.split() if int(num) >= 0]
number.sort(reverse= False)
for num in number:
    print(num, end=" ")
#  Elements in a range

user_input = input()
numbers = [int(num) for num in user_input.split()]
lower, upper = [int(num) for num in input().split()]

for num in numbers:
    if lower <= num <= upper:
        print(num, end=" ")

#  Contact list

# Get the list of name-phone number pairs

#  get the list of name, phone number pairs

user_input = input().split()
pairs = {}
for pair in user_input:
    name, phone_num = pair.split(',')
    pairs[name] = phone_num
#  get the name to search for

search_name = input().strip()
print(pairs[search_name])

#  Check if list is sorted

def in_order(nums):
    return nums == sorted(nums)

if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')

"""
