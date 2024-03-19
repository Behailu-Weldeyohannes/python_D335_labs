
#  ********* Chapter Five: Functions ********
"""
#  pizza size

def calc_pizza_area():
    pi_val = 3.14159265
    pizza_diameter = 12.0
    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    return pizza_area

print(f"{12:.1f} inch pizza is {calc_pizza_area():.3f} square inches")
def get_pattern():
    return '*****'
result = get_pattern()
print(result)
#  convert minutes to hours

def get_minutes_as_hours(orig_minutes):
    hours = minutes / 60
    return hours


minutes = float(input())
print(get_minutes_as_hours(minutes))

def calc_total_inches(feet, inches):
    total_inches = (feet *  12) + inches
    return total_inches
feet = int(input())
inches = int(input())

print(calc_total_inches(feet,inches))

def calc_pyramid_volume(length, width, height):
    area = length * width
    volume = (area * height) * 1/3
    return volume
length = float(input())
width = float(input())
height = float(input())
print(f"Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}")


#  print function
def print_greatest(word):
    print('--The Greatest *', end='')
    print(word, end='')
    print('* on Earth!--')

word = 'Love'
print_greatest(word)


def print_price(price):
    print(f"Price: ${price}")

product_price = 29
tax_amount = 6
print_price(product_price + tax_amount)
def print_operation(number1, number2):
    print(f'{number1} + {number2} = {number1 + number2}')

even_number = 6
odd_number = 1
print_operation(even_number, odd_number)
def print_info(name, age):
    print(f'{name}, {age}')

user_name1 = 'Ann'
user_name2 = 'Joe'
user_age1 = 18
user_age2 = 23
   
print_info(user_name1, user_age1)
print_info(user_name2, user_age2)
def print_points(name, age, total_points):
    print(f'{name} is {age}')
    print(f'{name} made {total_points} points')

user_name = 'Bob'
user_age = 24
regular_time_points = 23
overtime_points = 6

print_points(user_name, user_age, regular_time_points + overtime_points)

def print_feet_inch_short(num_feet,num_inches):
    print(f'{num_feet}\' {num_inches}"')

user_feet = int(input())
user_inches = int(input())

print_feet_inch_short(user_feet, user_inches) # Will be run with (5, 8), then (4, 11)

#  unit-conversion calculation.

def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled


miles_per_hour = float(input())
minutes_traveled = float(input())
print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')
# result = mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)
# print(f'Miles: {result:f}')

# miles_per_hour = float(input())
# minutes_traveled = float(input())
# hours_traveled = minutes_traveled / 60.0
# miles_traveled = hours_traveled * miles_per_hour

# print(f'Miles: {miles_traveled:f}')

#  temp from celsius to fahrenheit

def c_to_f(c):
    f = c * 9/5 + 32

    return f
c = float(input())

temp_f = c_to_f(c)

print(temp_f)

#  Calling functions in expressions

def compute_square(num_to_square):
    return num_to_square * num_to_square
c2 = compute_square(7) + compute_square(9)
print('7 squared plus 9 squared is: ', c2)

def find_max(num1, num2):
    max_val = 0.0

    if (num1 > num2):
        max_val = num1
    else:
        max_val = num2
    return max_val
max_sum = 0.0
a = float(input())
b = float(input())
y = float(input())
z = float(input())

max_sum = find_max(a,b) + find_max(y,z)

print('max_sum is:', max_sum )

#  calculates cylinder volume and surface area 
import math
def calc_circular_base_area(radius):
   return math.pi * radius * radius
def calc_cylinder_volume(baseRadius, height):
   return calc_circular_base_area(baseRadius) * height
def calc_cylinder_surface_area(baseRadius, height):
   return (2 * math.pi * baseRadius * height) + (2 * calc_circular_base_area(baseRadius))
radius = float(input('Enter base radius: '))
height = float(input('Enter height: '))
print('Cylinder volume: ' + f'{calc_cylinder_volume(radius, height):.3f}')
print('Cylinder surface area: ' + f'{calc_cylinder_surface_area(radius, height):.3f}')

def calc_base_area(base_length, base_width):
    return base_length * base_width

def calc_pyramid_volume(base_length,base_width, pyramid_height):
    base_area = calc_base_area(base_length, base_width)
    volume = base_area * pyramid_height * 1/3
    return volume

length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')

#  Functions with branches/loops

def calc_ebay_fee(sell_price):
    
    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price*p50)
    elif sell_price <= 1000:
        fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
    else:
        fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
                  + ((sell_price-1000)*p1000)
    return fee
selling_price = float(input('Enter item selling price (ex: 65.00): '))
print('eBay fee: $', calc_ebay_fee(selling_price))
"""
