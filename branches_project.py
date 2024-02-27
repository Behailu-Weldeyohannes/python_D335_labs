
#  ************* Branching ***************

#  Remove gray from RGB

# Given RGB values
red = int(input())
green = int(input())
blue = int(input())

# Remove the gray component from each color
gray_intensity = min(red, green, blue)
red -= gray_intensity
green -= gray_intensity
blue -= gray_intensity

# Ensure values stay within the valid range (0-255)
red = max(0, min(red, 255))
green = max(0, min(green, 255))
blue = max(0, min(blue, 255))

# Output the updated RGB values
print(f"{red} {green} {blue}")

str1 = input()
str2 = input()

# if len(str1) == len(str2):
#     print(str2)
# elif str1 > str2:
#     print(str1)
# else:
#     print(str2)

if len(str1) == len(str2):
    print(str2)
else:
    longest_str = max(str1, str2, key= len)
    print(longest_str)

#  max2
value1 = int(input())
value2 = int(input())
if value1 > value2:
    print(value1)
else:
    print(value2)

#  Max of 3
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2 == num3:
    print(num1)
else:
    greatest = max(num1, num2, num3)
    print(greatest)

# Type your code here
service = input("Enter desired auto service:\n")
print(f"You entered: {service}")
#  part 2
oil_change = 35
tire_rotation = 19
car_wash = 7
if service == "Oil change":
    print(f"Cost of oil change: ${oil_change}")
elif service == "Tire rotation":
    print(f"Cost of tire rotation: ${tire_rotation}")
elif service == "Car wash":
    print(f"Cost of car wash: ${car_wash}")
else:
    print("Error: Requested service is not recognized")

#Automobile service invoice
# Type your code here
# Type your code here

services= {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12
}

# Output the menu
print("Davy's auto shop services")
for service, cost in services.items():
    print(f"{service} -- ${cost}")
# Prompt the user for two services from the menu
print("\nSelect first service:")
service1 = input()
print("Select second service:")
service2 = input()
print()
# Output the cost for each service and the total cost
cost1 = services.get(service1,0) 
cost2 = services.get(service2,0) 
total = cost1 + cost2
print("Davy's auto shop invoice\n")
print(f"Service 1: {service1}, ${cost1}" if cost1 != 0 else "Service 1: No service")
print(f"Service 2: {service2}, ${cost2}" if cost2 != 0 else "Service 2: No service")
print()

print(f"Total: ${total}")

 
#  median of 3
#  Write a program that takes in three integers and outputs the median value
num1 = int(input())
num2 = int(input())
num3 = int(input())
numbers = [num1, num2, num3]
numbers.sort()
median = numbers[1]
print(median)

#  median of 4
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
# num5 = int(input())

# Sort the numbers
sorted_numbers = sorted([num1, num2, num3, num4])

# Calculate the median
n = len(sorted_numbers)
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    middle_left = sorted_numbers[n // 2 - 1]
    middle_right = sorted_numbers[n // 2]
    median = (middle_left + middle_right) / 2

print('Median:', median)


#  speeding ticket
# Type your code here.
sl = int(input())
ds = int(input())
speed_dif = ds - sl
ticket = 0

if speed_dif >= 41:
    ticket = 300
elif speed_dif >= 21:
    ticket = 150
elif speed_dif >= 6:
    ticket = 75
elif speed_dif <= -10:
    ticket = 50
else:
    ticket = 0
print(ticket)


#  movie ticket prices

day = input().lower()
age = int(input())
price = 0
day_price = 0
night_price = 0

if age < 4:
    if day == "day" or day == "night":
        day_price = 0
        night_price = 0
elif age >= 4:
    if day == "day":
        day_price = 8
    elif day == "night":
        if age <= 16:
            night_price = 12
            day_price = None
        elif age <= 54:
            night_price = 15
            day_price = None
        else:
            night_price = 13
            day_price = None
if day_price == 0 and night_price == 0:
    print("free")
elif day_price != None:
    print(f"${day_price}")
else:
    print(f"${night_price}")
 
#  How many digits

# Type your code here.
num = int(input())

if 0 <= num <= 9999:
    num_digit = len(str(num))
    if num_digit >= 2:
        print(f"{num_digit} digits")
    else:
        print(f"{num_digit} digit")
    