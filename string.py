"""
st1 = 'hey there he said \\"hi" hello'
st2 = 'hey there he said \"hi" hello'
# print(st1)
# print(st2)
print(st1[4])
print(st1[4:7])
print(st1[4:7:2])
print(st1[:7])
print(st1[:-7])
print(st1[1:])
print(st1[:-1])

my_str = '''I 
am  a  
Geek!!!
'''

# print(my_str)

#  get middle
str3 = 'hey there he said "hi" hello'
def get_middle(str3):
    print("Orig String", str3)
    mid = int(len(str3)/ 2)
    result = str3[mid - 1:mid + 2]
    print(result)
get_middle("My dog likes bones.")


str4 = "Hello World!"

print("Updated String", str4[:6] + "Python")

str5= "This is cool"
newstr = str5[::-1]  # reverse 
print(newstr)

format_string = '{name:>26}{phone:*>12}'
print(format_string.format(name= "Peter Challa", phone="8675309"))
print(format_string.format(name= "James John", phone="1675309"))


print("{:.6f}".format(548.22))
print("{:.6f}".format(548.2277898788778))

st1 = "hello"
st2 = "Python"

print(st1 + " " + st2)
print(st1.count(st1,0,len(st1)))


#  find

str = "Python"
st = "python i'm gonna replace something in here"

# print(str.find("P"))
# print(st.replace("replace", "change"))
# print(st.upper())
# print(st.lower())
print(st.capitalize())
# print(st.title())

text = "the rain in spain messes up my hair"
if text == "the rain":
    print("false")
else:
    print("true")

st = "abc234 easy as 123"

# print(st.isdigit())
# print(st.startswith('a'))

# print(st.isspace())
nums = ['1','2','3','1','4']
# print(st.split())
print(','.join(nums))


input = input()
# input_b = str(input)
if input.isdigit():
    print("True")
else:
    print("false")

name = input()
parts = name.split()
# print(parts)
#  Julia Clark to Clark, J.
#  Pat Silly Doe to Doe P.S.
if len(parts) == 2:
    print(f"{parts[1]}, {parts[0][0]}.")
elif len(parts) == 3:
    print(f"{parts[2]}, {parts[1][0]}.{parts[0][0]}.")

#  count characters
#  n Nobody
input_str = input()
char = input_str[0]
new_str = input_str[1:]

if char == "1":
    # print(f"{new_str.count(char)} {char}")
    print(f"1 {new_str}")
else:
    count = new_str.count(char)
    if count ==1:
        print(f"1 {char}")
    else:
        # print(f"{new_str.count(char)} {char}'s")
        print(f"{count} {char}'s")

#  remove all non-alpha characters

user_input = input()
no_spaces = ""

for char in user_input:
    if char.isalnum() and not char.isdigit():
        no_spaces = no_spaces + char
print(no_spaces)

# Acronyms
#  get input from the user 
input_phrase = input()
# split the input in to words
words = input_phrase.split()
# print(words)
#  Initialize an empty string for the acronmy
acronmy = ""
# find the acronmy 

for word in words:
    if word[0].isupper():
        acronmy = acronmy + word[0] + "."
print(acronmy)

#  contains the character

search_char = input()
#  read list of words from the user 
word_list = input().split()
#  initialize empty list
result_words = []
#  check each word in the list
for word in word_list:
    if search_char in word:
        result_words.append(word)
#  print the result
for result_word in result_words:
    print(result_word)


def check_character(word, index):
    if 0 <= index < len(word):
        char = word[index]
        if char.isalpha():
            return f"Character '{char}' is a letter"
        elif char.isdigit():
            return f"Character '{char}' is a digit"
        elif char.isspace():
            return f"Character '{char}' is a white space"
        else:
            return f"Character '{char} is unknown'"
    else:
        return "Index out of range"
#  read in put from the user
word = input()
index = int(input())
result = check_character(word, index)
print(result)

#  remove digits
user_input = input()
#  initialize
result = ""
# loop through
for char in user_input:
    if not char.isdigit():
        result = result + char
print("Out put:", result)

#  midfix of 3

user_input = input()
mid_index = len(user_input) // 2
start_index = mid_index -1 
end_index = mid_index + 2

midfix = user_input[start_index:end_index]
print(midfix)

#  prefix of 3

user_input = input()

prefix = user_input[:3]
print(prefix)

#  postfix of 3
user_input = input()

postfix = user_input[-3:]
print(postfix)

#  login name with three user inputs
f_name = input()
l_name = input()
user_int = int(input())
login_name = f"{l_name[:5]}{f_name[:1]}{user_int % 100}"
print(login_name)

#  username from one input
user_input = input()
name_and_num = user_input.split()
# extract full name and number

full_name = ' '.join(name_and_num)[:-1]
number = name_and_num[-1]

#  extract last name f_letter and 2 digits

l_name = full_name.split()[:-1]
f_letter = full_name[0]
last_two_dig = number[-2]
#  determine the 5 letter of  last name
five_last_name = l_name[:5]
print(five_last_name)

user_input = input()
name_and_number = user_input.split()
# extract full name and number
number = name_and_number[-1]
l_name = name_and_number[1]
f_name = name_and_number[0]
#  extract based on the requirements
login_name = f"{l_name[:5]}{f_name[:1]}{number[2:]}"
print(f"Your login name: {login_name}")


#  parsing strings

user_input = ""
while user_input.lower() != 'q':
    # Prompt the user for input
    user_input = input("Enter input string:\n")

    # Check if the input string contains a comma
    if ',' in user_input:
        # Split the input string into two names
        names = user_input.split(',')

        # Remove leading and trailing whitespaces from each name
        name1 = names[0].strip()
        name2 = names[1].strip()

        # Output the two words
        print("First word:", name1)
        print("Second word:", name2)
    else:
        # Report an error if the input string does not contain a comma
        print("Error: No comma in string.")
        """




   






