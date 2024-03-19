"""
my_list = [21.42, "footbar", 3, 4, "bark", False, 3.14]
# print(my_list[::-1]) # reverse  

if 21.42 in my_list:
    print("Bingo!")
if "sheeba" not in my_list:
    my_list.append("sheeba")
print(my_list)

my_list[3] = "fountain"
print(my_list)
my_list2 = my_list.copy()
print(my_list2)

my_list3 = [21.42, "footbar", 3, 4, "bark", False,21.42, 21.42, 3.14]

x = my_list3.count(21.42)
# print(x)

y = my_list3.index('bark')
print(y)
my_list3.insert(1, "orange")
print(my_list3)

my_list3.pop(1)
print(my_list3)
my_list4 = [21.42, "footbar", 3, 4, "bark", False,21.42, 21.42, 3.14]
# my_list4.remove('footbar')
# print(my_list4)
# my_list4.reverse()
# print(my_list4)
# print(my_list4)
my_list5 = ['aa', 'bbb', 'ccc','dddd']
# my_list5.sort()
# print(my_list5)
new = sorted(my_list5, reverse=True)
print(new)
my_list6 = [21.42, 21.42, 21.42, 3, 4, 3.14123]
my_list4 = [21.42, "footbar", 3, 4, "bark", False,21.42, 21.42, 3.14]
print(len(my_list6))
my_list7 =my_list6 + my_list4 
# print(my_list7)
print(min(my_list6))
print(max(my_list6))
print(sum(my_list6))
my_list = [16, 29, 45, 83, 16, 25, 45]
# new_list = []
# for i in my_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
my_list5 = [3.2, 5.0, 16.5, 12.25]
for i in range(len(my_list5)):
    my_list5[i] += 6
print(my_list5)
usernum = input()
parts = usernum.split()
nums = []
for pos, part in enumerate(parts):
    nums.append(int(part))
    # print("{} {}".format(pos, part))
    print(f"{pos} {part}")
total = 0

for num in nums:
    total = total + num
    print(total)
mylist = [ 50, 23, -4]
mynewlist = [(i-10) for i in mylist]
print(mynewlist)
mylist2 = [30, 40, 50, 10]
newlist = [(i // 2) for i in mylist2]
print(newlist)
evens = [i for i in range(10) if i % 2 == 0]
print(evens)
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
print(result)
odds = [i for i in range(10) if i % 2 != 0]
print(odds)
#  middle item for odd int
input_num = input().split()
num = [int(num) for num in input_num]
#  check if the numbers exceeds 9
if len(num) > 9:
    print("Too many inputs")
else:
    #  find the middle index
    middle_index = len(num) // 2
    print(num[middle_index])
input_num = input().split()
num = [int(num) for num in input_num]
# print(num)
if len(num) > 9:
    print("Too many inputs")
else:
    mid_index = len(num) // 2
    print(num[mid_index])
input_num = input().split()
number = [int(num) for num in input_num]
if len(number) > 9:
    print("Too many inputs")
else:
    middle_index = len(number) // 2
#  out put the average of the two middle ints
    middle_sum = number[middle_index - 1] + number[middle_index]
    print(middle_sum)
    # middle_avg = middle_sum / 2
    middle_avg = middle_sum // 2
    print(middle_avg)
# Input a list of words separated by spaces
input_string = input("Enter a list of words: ")

# Create a dictionary to store word counts
word_counts = {}

# Iterate through the words, updating counts
for word in input_string.split():  # Split into words
    if word in word_counts:
        word_counts[word] += 1 
    else:
        word_counts[word] = 1 

# Print the unique words and their frequencies
for word, count in word_counts.items():
    print(word, count)
list = 'hey hi Mark hi mark'
text = list.split()

for word in text:
        freq = text.count(word) 
        print(word, freq)

#  Replacement words
sent1 = input().split()
sent2 = input().split()

for word1, word2 in zip(sent1,sent2):
    if word1 != word2:
        print(word1, word2)
#  combine using zip()
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
#  using zip combine the list
zipped_result = zip(list1,list2)
#  convert the result to a list
result_list = list(zipped_result)
print(zipped_result)
print("------------")
print(result_list)

input1 = input()
input2 = input()

for word1, word2 in zip(input1, input2):
    if word1 != word2:
        print(word1, word2)
print("word1\tword2")
print("-----------")
#  scrabble points
tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }  
input_word = input().upper()
total_value = sum(tile_dict[letter] for letter in input_word if letter in tile_dict)
print(total_value)
dict_value = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
             'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
             'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
#  perform addition, subtraction, multiplication, and division
#  addition
data_sets = input().upper()
total_sum = sum(dict_value[chara] for chara in data_sets if chara in dict_value)
# print(total_sum)
#  subtraction
data_sets = input()
subtract = data_sets.upper()
subtracted_value = sum(-dict_value[char] for char in subtract if char in dict_value)
# print(subtracted_value)
# print(data_sets)

dict_value = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
             'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
             'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
#  calculate total of the values
# total_sum = sum(dict_value.values())
# print(total_sum)

total = sum(dict_value.values())
print(total)
# Reverse list
def reverse_list(letters):
    reversed_list = list(reversed(letters))
    return reversed_list
input_string = input()
original_list = input_string.split()
reversed_result = reverse_list(original_list)
print(reversed_result)
input_string = input()
original_list = input_string.split()
original_list.reverse()
print(original_list)
#  Remove all even numbers from a list

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_num = [num for num in input_list if num % 2 != 0]
print(odd_num)

#  remove all odd numbers from the list

even_num = [num for num in input_list if num % 2 == 0]
print(even_num)
#  Output values below an amount
threshold = int(input())
int_list = []
while True:
    num = int(input())
    if num == -1:
        break
    int_list.append(num)
#  output int less than or equal to the threshold value
    result_list = [num for num in int_list if num <= threshold]
    print(result_list)
"""
#  Adjust list by normalizing
























