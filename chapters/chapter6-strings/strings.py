
#  ********* Chapter 6: Strings ********

"""
url = 'http://en.wikipedia.org/wiki/Turing'
domain = url[7:23]
domain2 = url[0:4]
print(domain2)

my_str = 'The cat in the hat'
print(my_str[0:3])

#  ----- Slicing and slicing operations 

#  , : is used for basic slicing to define the start and end indices, while :: is used for extended slicing

my_str = "The cat jumped the brown cow"
animal = my_str[4:7]
print(f"The animal is a {animal}")

my_str = 'The fox jumped the brown llama'
print('The animal is still a', animal)  # animal variable remains unchanged.
# The slice stride
# omitting start, end indices.
user_text = input('Enter a string: ')
print()
first_half = user_text[:len(user_text)//2]
last_half = user_text[len(user_text)//2:]
print(f'the first half: {first_half}')
print(f'the second half: {last_half}')


text = "wikipedia.org/wiki/"
my_str = text[10:-5]
print(my_str)

my_str = 'http://reddit.com/r/python'
protocol = 'http://'
print(my_str[len(protocol):])

my_str = 'Agt2t3afc2kjMhagrds!'
print(my_str[0:5:1])

my_str2 = 'Agt2t3afc2kjMhagrds!'
print(my_str2[::2])
state = 'Texas'
my_slice = state[1:5]
print(my_slice)

start_index = int(input())
end_index = int(input())
rhyme_lyric = 'The cow jumped over the moon.'
sub_lyric = rhyme_lyric[start_index:end_index]
print(sub_lyric)

# state = 'Maine'
# print(my_slice)
numbers = '0123456789'
print(f"All numbers: {numbers[::]}")
print(f"All even numbers: {numbers[::2]}")
print(f"Every third num between 1 and 8: {numbers[1:9:3]}")


#  Advanced string formating

name = 'Bob'
print(f"{name:5}")
name = "Jane"
points = 12
print(f"{name:6}{points:4}")

name = 'Jack'
matches = 30
points = 7
print(f"{name:8}{points:3}{matches:4}")
#  Aligning text
#  alignment options include left-aligned '<', right-aligned '>' and centered '^'.

print(f"{Bob}:<5")

#  fill
score = 18

print(f"{score:0>4}") # 0009
print(f"{score:4}") # 0009
print(f"{score:*>4}") # 0009
print(f"{score:0^4}") # 0009
name = "Wayne Rooney"
goals = 36

print(f"{name:<16}{goals:>6}")
print(f"{name:_<16}{goals:0>6}")

#  Floating-point precision
print(f'{5:4.1f}')

#  string method

# replace(old, new)
# replace(old, new, count) only replaces the first count occurrences of old

phrase = 'Someday I will have three goats, six horses, and nine llamas.'
phrase = phrase.replace('one', 'uno')
phrase = phrase.replace('two', 'dos')
phrase = phrase.replace('three', 'tres')
phrase = phrase.replace('four', 'cuatro')
print(phrase)

#  find()
my_str = 'Boo Hoo!'
# print(my_str.find('!'))
#  find(x, start) # begins the search at index start:
result = my_str.find('oo',5)
# print(result)
my_str.find('oo', 2, 3)
# rfind(x) searches the string in reverse
#  count(x) Returns the number of times x occurs in the string.
yes = my_str.count('oo')
print(yes)

#  Comparing strings
#  Identity vs. equality operators.

# if student_name == 'Amy Adams':
#     print('Equality operator: True')
# else:
#     print('Equality operator: False')
#  methods are available to help manage string comparisons

isalnum() -- Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
isdigit() -- Returns True if all characters are the numbers 0-9.
islower() -- Returns True if all cased characters are lowercase letters.
isupper() -- Return True if all cased characters are uppercase letters.
isspace() -- Return True if all characters are whitespace.
startswith(x) -- Return True if the string starts with x.
endswith(x) -- Return True if the string ends with x.
print('HTTPS://google.com'.isalnum())
'HTTPS://google.com'.startswith('HTTP')
'\n \n'.isspace()
print('1 2 3 4 5'.isdigit())
'LINCOLN, ABRAHAM'.isupper()

#  Creating new strings from a string. Below are Methods to create new strings:

# capitalize() -- Returns a copy of the string with the first character capitalized and the rest lowercased.
# lower() -- Returns a copy of the string with all characters lowercased.
# upper() -- Returns a copy of the string with all characters uppercased.
# strip() -- Returns a copy of the string with leading and trailing whitespace removed.
# title() -- Returns a copy of the string as a title, with first letters of words capitalized.


user_tweet = input()
if 'LOL' in user_tweet:
    print('LOL means laughing out loud.')
else:
    print('No abbreviation.')

user_tweet = input()

decoded_tweet = user_tweet.replace('TTYL', 'talk to you later')
print(decoded_tweet)

#  Splitting and joining strings
#  The split() method
string = 'Music/artist/song.mp3'
my_token = string.split('/')
print(my_token)
file = 'C:/Users/Charles Xavier//Documents//report.doc'
separator = '/'
results = file.split(separator)
print(f"Separator({separator}):", results)

song = "I scream; you scream; we all scream, for ice cream.\n"
s = song.split()
a = song.split('\n')
b = song.split('scream')
print(s)
print(a)
print(b)
#  join() performs the inverse operation of split() by joining a list of strings together to create a single string.
web_path = [ 'www.website.com', 'profile', 'settings' ]
separator = '/'
url = separator.join(web_path)
# print(url)
phrases = ['To be, ', 'or not to be.\n', 'That is the question.']
sentence = ''
for phrase in phrases:
    sentence = sentence + phrase
    print("this is the result: ",sentence)
phrases = ['To be, ', 'or not to be.\n', 'That is the question.']
sentence = "".join(phrases)
print(sentence)

x = ['images', 'google', 'com']
my_str = ".".join(x)
# print(my_str)

y = ['New', 'York']
my_str = "".join(y)
print(my_str)
#  Using the split() and join() methods together
path = input('Enter file name: ')
new_separator = input('Enter new separator: ')
tokens = path.split('/')
print(new_separator.join(tokens))
title = 'Python-Lab-Warmup'
tokens = title.split('-')
title = title.replace('-',':')
tokens = ":".join(tokens)
print(tokens)
# print(tokens)
item_info = 'Book 13 14'
item_tokens = item_info.split()
print(item_info)
item = item_tokens[0]
print(item)
quantity = item_tokens[1]
price = item_tokens[2]
print(item, 'stock:', quantity)
print('Price:', price)
item_info = 'Hat 11 16'

item_tokens = item_info.split()
item = item_tokens[0]
quantity = item_tokens[1]
price = item_tokens[2]

print(item, 'stock:', quantity)
print('Price:', price)

phone_number = '202-555-0169'

separator = ':'
phone_number_tokens = phone_number.split('-')
print(separator.join(phone_number_tokens))
phone_number = input()
number_segments = phone_number.split('-')
area_code = number_segments[0]
print(number_segments)
print(area_code)

user_input = input()
if user_input.isdigit():
    print("Yes")
else:
    print("No")

name = input()
parts = name.split()
print(parts)
if len(parts) == 2:
    print(f"{parts[1]}, parts[0][0].")
elif len(parts) == 3:
    print(f"{parts[2]}, {parts[0][0]}.{parts[1][0]}.")

u_input = input()
char = u_input[0]
new_str = u_input[1:].replace(" ", "")
# print(new_str)
if new_str.count(char) == 1:
    print(f"1 {char}")
else:
    print(f"{new_str.count(char)} {char}'s")
# Mad Lib - loops

while True:
    user_input = input().split()
    word = user_input[0]
    if word == 'quit':
        break
    count = int(user_input[1])
    print(f"Eating {count} {word} a day keeps the doctor away.")

#  remove all non-alpha characters
user_input = input()
no_spaces = ""
for char in user_input:
    if char.isalnum() and not char.isdigit():
        no_spaces = no_spaces + char
print(no_spaces)

# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    print(mystring[:x])

printFirst('WGU College of IT', 3) # output: WGU
printFirst('WGU College of IT', 11) # output: WGU College

printFirst('Hi', 1) # out put H
#  prints last
def getLast(my_str, x):
    result = my_str[x:]
    print(result)
getLast("Love You", 5)

def contains_word(mystr):
    if 'WGU' in mystr:
        print(True)
    else:
        print(False)
contains_word("WGU college of IT")
"""
