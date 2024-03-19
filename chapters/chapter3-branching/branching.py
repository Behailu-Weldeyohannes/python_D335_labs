
#  ********* Chapter Three: Branching ********
"""

#  detecting equal values

user_num = int(input())
div_remainder = user_num % 2

if div_remainder == 0:
    print(f'{user_num} is even.')
else:
    print(f'{user_num} is odd.') 
bonus_val = 15
num_items = 44

if bonus_val == 14:
    num_items = num_items + 3
else:
    num_items = num_items + 6

num_items = num_items + 1
print(num_items)
bonus_val = 12

if bonus_val == 12:
    bonus_val = bonus_val + 2 
    bonus_val = 3 * bonus_val

else:
    bonus_val = bonus_val + 10
print(f"{bonus_val}")
num_years = int(input('Enter number years married: '))

if num_years == 1:
    print('Your first year -- great!')
elif num_years == 10:
    print('A whole decade -- impressive.')
elif num_years == 25:
    print('Your silver anniversary -- enjoy.')
elif num_years == 50:
    print('Your golden anniversary -- amazing.')
else:
    print('Nothing special.')

#  Detecting ranges using logical operators
user_channel = int(input())
if (user_channel >= 2) and (user_channel <= 499):
   channel_type = 's'

elif (user_channel >= 1002) and (user_channel <= 1499):
   channel_type = 'h'

else:
   channel_type = 'e'

#  Detecting ranges with gaps
movie_ticket_price = None

user_age = int(input('Enter your age: '))

if user_age <= 12:     # Age 12 and under
   print('Child ticket discount.')
   movie_ticket_price = 11
elif user_age >= 65:   # Age 65 and older
   print('Senior ticket discount.') 
   movie_ticket_price = 12
else:                  # All other ages
   movie_ticket_price = 14

print(f'Movie ticket price: {movie_ticket_price}')
car_year = int(input())
if car_year < 1967:
    print("Probably has few safety features.")
if car_year > 1971:
    print("Probably has head rests.")
if car_year > 1990:
    print("Probably has electronic stability control.")
if car_year > 2002:
    print("Probably has airbags.")

car_year = int(input())

if car_year < 1967:
    print("Probably has few safety features.")
elif car_year > 1971:
    print("Probably has head rests.")
    if car_year > 1990:
        print("Probably has electronic stability control.")
        if car_year > 2002:
            print("Probably has airbags.")
user_num1 = int(input())
user_num2 = int(input())

if user_num1 < 0:
    print("user_num1 is negative.")
if user_num2 > 8:
    user_num2 = 1
else:
    print("user_num2 is less than or equal to 8.")

print('user_num2 is', user_num2)
#  Membership operators: in/not in
# -----------Use the "in" operator --------
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name in barcelona_fc_roster:
    print('Found', name, 'on the roster.')
else:
    print('Could not find', name, 'on the roster.')
# Use the "not in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name not in barcelona_fc_roster:
    print('Could not find', name, 'on the roster.')
else:
    print('Found', name, 'on the roster.')
# ----------- Identity operators: is/is not----------

w = 500
x = 500 + 500  # Create a new object with value 1000
y = w + w      # Create a second object with value 1000
z = x          # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object')
if z is not y:
    print('z and y are NOT bound to the same object')

my_dict = {'A': 1, 'B': 2, 'C': 3}
if 'B' in my_dict:
   print("Found 'B'")
else:
   print("'B' not found")
# Membership operator does not check values
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')
word = 'rug'
vowel = input()

if vowel in word:
    print('in')
else:
    print('not in')

a = 'panda'
b = 'otter'
c = [a, b]
d = c
d[0] = 'dog'

if (b is d[1]):
    print('f')
if (a is d[0]):
    print('g')
if (c is d):
    print('h')

# First code block has no indentation

model = input('Enter car model: ')
year = int(input('Enter year of car manufacture: '))

antique = False
domestic = False

if year < 1970:
    # New code block has indentation of 4 columns
    antique = True

# Back to code block 0

if model in ['Ford', 'Chevrolet', 'Dodge']:
  # New code block has indentation of 2 columns
  # Any amount of indentation > 0 is OK.
  domestic = True

# Back to code block 0

if antique:
    # New code block has indentation of 4 columns
    if domestic:
        # New block has 4 additional columns (8 total)
        print('My own model-T still runs like a charm...')


user_val = int(input())

cond_str = "negative" if user_val < 0 else "non-negative"

print(user_val, 'is', cond_str)
num_users = int(input())
update_direction = int(input())

num_users = num_users + 1 if update_direction == 3 else num_users -1

print('New value is:', num_users)

#  tweet decoder
# Dictionary to store abbreviations and their meanings
abbreviations_dict = {
    'LOL': 'laughing out loud',
    'BFN': 'bye for now',
    'FTW': 'for the win',
    'IRL': 'in real life',
    # Add more abbreviations as needed
}

# Get input tweet from the user
tweet = input('Enter the tweet:\n')

# Split the tweet into words
words = tweet.split()

# Dictionary to store decoded abbreviations
decoded_abbreviations = {}

# Check each word for abbreviations
for word in words:
    # Check if the word is an abbreviation
    if word.upper() in abbreviations_dict:
        decoded_abbreviations[word.upper()] = abbreviations_dict[word.upper()]

# Print the decoded abbreviations
if decoded_abbreviations:
    print('Decoded abbreviations:')
    for abbreviation, meaning in decoded_abbreviations.items():
        print(f'{abbreviation} = {meaning}')
else:
    print('No abbreviations found in the tweet.')

#  Interstate highway numbers

highway_number = int(input())

if 1 <= highway_number <= 99:
    if highway_number % 2 == 0:
        print(f'I-{highway_number} is primary, going east/west.')
    else:
        print(f'I-{highway_number} is primary, going north/south.')
elif 100 <= highway_number <= 999:
    primary_highway = highway_number % 100
    if 1 <= primary_highway <= 99:
        direction = "north/south" if primary_highway % 10 == 0 or primary_highway % 10 == 5 else "east/west"
        print(f'I-{highway_number} is auxiliary, serving I-{primary_highway}, going {direction}.')
    else:
        print(f'{highway_number} is not a valid interstate highway number.')
else:
    print(f'{highway_number} is not a valid interstate highway number.')

#  Seasons
# Get input for the month and day
month = input('Enter the month: ')
day = int(input('Enter the day: '))

# Convert month to lowercase for case-insensitivity
month_lower = month.lower()

# Check the season based on the given date
if (month_lower == 'march' and day >= 20) or (month_lower == 'april' or month_lower == 'may') or (month_lower == 'june' and day <= 20):
    season = 'Spring'
elif (month_lower == 'june' and day >= 21) or (month_lower == 'july' or month_lower == 'august') or (month_lower == 'september' and day <= 21):
    season = 'Summer'
elif (month_lower == 'september' and day >= 22) or (month_lower == 'october' or month_lower == 'november') or (month_lower == 'december' and day <= 20):
    season = 'Autumn'
elif (month_lower =='december' and day >= 21) or (month_lower == 'january' or month_lower == 'february') or (month_lower == 'march' and day <= 19):
    season = 'Winter'
else:
    print("Invalid")

input_month = input()
day = int(input())

month = input_month.lower()
year = 2024

if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
    print('Invalid')
elif day <= 0:
    print('Invalid')
else:
    days_in_month = {
        'january': 31,
        'february': 29 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }

    if day > days_in_month[month]:
        print('Invalid')
    else:
        if (month == "march" and day >= 20) or (month == 'april' or month == 'may') or (month == 'june' and day <= 20):
            print("Spring")
        elif (month == 'june' and day >= 21) or (month == 'july' or month == 'august') or (
                month == 'august' and day <= 21):
            print("Summer")
        elif (month == 'september' and day >= 22) or (month == 'october' or month == 'november') or (
                month == 'december' and day <= 20):
            print("Autumn")
        elif (month == 'december' and day >= 21) or (month == 'january' or month == 'february') or (
                month == 'march' and day <= 19):
            print("Winter")

#  leap year
year = int(input())
if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print(f"{year} - leap year")
else:
    print(f"{year} - not a leap year")

#  golf score
par = int(input())
strokes = int(input())

if par in [3, 4, 5]:
    if strokes == par - 2:
        print("Eagle")
    elif strokes == par - 1:
        print("Birdie")
    elif strokes == par:
        print("Par")
    elif strokes == par + 1:
        print("Bogey")
    else:
        print("Error")
else:
    print("Error")

"""
