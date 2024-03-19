#  ********* Chapter One: Variables ********
#  variable assignment with math function
import math

"""
import math
x = 2.3
z = math.ceil(x)
print(z)
y = 4.5
y = math.pow(math.floor(z), 2.0)  # power 
print(y)


a = 15.75
b = math.sqrt(math.ceil(a)) # squar root base with ceil 
print(b)

c = 4
d = math.factorial(c)
print(d) # The factorial of 4 is 4 * 3 * 2 * 1 = 24: 4! = 4 * 3 * 2 * 1 = 24 

x = math.sqrt(64.0)
print(x)
x = math.fabs(-3.7)
print("X: ",x) #  absolute value
x = math.fabs(-3.7)
y = abs(-3.7) #  absolute value
print("Y: ",y)

result = math.pow(5.0, 3.0) # 5 * 5 * 5  
print(result)

abs = math.fabs(-14.0 + 3.0)
print(abs)
calc = math.pow(4.0, math.sqrt(9.0))
print(calc)
import math

x = float(input())
y = float(input())

z = math.sqrt(y-x) 
print(f"{z:.2f}")

x = float(input())
y = float(input())
z = y + math.sqrt(x)
print(f"{z:.2f}")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point_dist = math.sqrt(pow(x2 - x1, 2) + pow(y2 -y1, 2))
print('Points distance:', point_dist)

# print(100/ 0)  error
# minutes to hours/minutes
minutes = int(input('Enter minutes:\n'))
hours = minutes // 60
minutes_remaining = minutes % 60

print(minutes, 'minutes is', end=' ')
print(hours, 'hours and', end=' ')
print(minutes_remaining, 'minutes.\n', end=' ')
#  converts seconds to hours and minutes
seconds = int(input('Enter seconds:\n'))

hours = seconds // 3600
remaining_seconds = seconds % 3600
minutes = remaining_seconds // 60

if hours == 1 and minutes == 1 and seconds == 1:
    print(f"{hours} hour, {minutes} minute, and {seconds} second")
elif hours == 1 and minutes == 1:
    print(f"{hours} hour, {minutes} minute, and {seconds} seconds")
elif hours == 1 and seconds == 1:
    print(f"{hours} hour, {minutes} minutes, and {seconds} second")
elif minutes == 1 and seconds == 1:
    print(f"{hours} hours, {minutes} minute, and {seconds} second")
elif hours == 1:
    print(f"{hours} hour, {minutes} minutes, and {seconds} seconds")
elif minutes == 1:
    print(f"{hours} hours, {minutes} minute, and {seconds} seconds")
elif seconds == 1:
    print(f"{hours} hours, {minutes} minutes, and {seconds} second")
elif hours == 0 and minutes == 0 and seconds == 0:
    pass  # Do nothing if all values are zero
else:
    print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")

# print('\\c\\users\\juan')
# print('My name is \'Tater Tot\'.')
# print('My name is \'Peter\'')
# print('10...\n9...')
# Raw strings 

# my_string = 'This is a \n \'normal\' string\n'
# my_raw_string = r'This is a \n \'raw\' string'

# print(my_string)
# print(my_raw_string)
my_str = r"C:\\file.doc"
my_str2 = r"C:\file.doc"
print(my_str)
print(my_str2)

#Number games (3 digit num)
input_num = int(input())
if 100 <= input_num <= 999:
    result = input_num * (7 * 11 * 13)
    output_num = int(str(result) + str(result))
    print(f"The 6-digit number is: {output_num}")
else:
    print("Please enter a valid 3-digit number")
#  2 digit num
num = int(input("Enter 2 digit number:\n"))
result = num * (3 * 7 * 13 * 37)
print(result)
#  3 digit
num = int(input("Enter 3 digit number:\n"))
result = num * (7 * 11 * 13)
print(result)
#  5 digit
num = int(input("Enter 5 digit number:\n"))
result = num * (11 * 9091)
print(result)
#  divide input integer
user_num = int(input())
div_num = int(input())
result1 = user_num // div_num
result2 = result1 // div_num
result3 = result2 // div_num
print(f"{result1} {result2} {result3}")
#  Expression for calories burned during workout
#  Calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368
age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())
calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368
print(f"Calories: {calories:.2f} calories")
import math
#  using math function
x = float(input())
y = float(input())
z = float(input())

x1 = pow(x,z)
x2 = pow(x,pow(y,z))
x3 = abs(x - y)
x4 = math.sqrt(pow(x,z))

print(f"{x1:.2f} {x2:.2f} {x3:.2f} {x4:.2f}")
# Musical note frequencies
initial_frequency = int(input())
r = pow(2, 1/12)
print(f"{initial_frequency:.2f} Hz")
#  calculate and print the next three higher key frequencies
for n in range(1,4):
    next_freq = initial_frequency * pow(r,n)
    print(f"{next_freq:.2f} Hz")
"""