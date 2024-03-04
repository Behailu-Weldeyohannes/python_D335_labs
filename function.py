
# def my_function():
#     print("Hello")
#     print("Bye")
# my_function()
"""

def square_this(num):
    return num * num

print(square_this(4))
# print(square_this(6))

def square_me(num):
    num = 5
    return num * num
print(square_me(4))


def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    return driven_miles * (1.0 / miles_per_gallon) * dollars_per_gallon

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

miles_10 = driving_cost(10, miles_per_gallon, dollars_per_gallon)
miles_50 = driving_cost(50, miles_per_gallon, dollars_per_gallon)
miles_400 = driving_cost(400, miles_per_gallon, dollars_per_gallon)

print(f"{miles_10:.2f}")
print(f"{miles_50:.2f}")
print(f"{miles_400:.2f}")



def greet():
    print("Hello")
    print("Hi")
    print("Greetings")

greet()

# print(greet())
 

def greet_with_name(name):
    print(f"Hello {name} ")
    print(f"Hi {name} ")
    print(f"How do you do {name} ")


greet_with_name("Peter")

#  positional argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What it it like in {location}")

greet_with("Konjo", "New York")

#  keyword argument
def greet_with(name="Konjo", location="New York"):
    print(f"Hello {name}\nWhat it is like in {location}")
greet_with()

n = int(input())
def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")
prime_checker(num=n)

#  outputs
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"
    # print(f"{formated_f_name} {formated_l_name}")
    print(formated_string)
    

num_laps = float(input())
def laps_to_miles(num_laps):
    return num_laps * 0.25
miles = num_laps * 0.25

print(f"{miles:.2f}")

def max_magnitude(a, b, c):
    abs_values = [abs(a), abs(b), abs(c)]
    max_abs_value = max(abs_values)

    if max_abs_value == abs(a):
        return a
    elif max_abs_value == abs(b):
        return b
    else:
        return c
a = int(input())
b = int(input())
c = int(input())

result = max_magnitude(a,b,c)
print(result)
"""








