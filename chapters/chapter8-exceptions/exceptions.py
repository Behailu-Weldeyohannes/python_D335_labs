
#  ********* Chapter Eight: Exceptions ********
"""

#  BMI example

user_input = ""
while user_input != 'q':
    try:
        weight = int(input())
        height = int(input())
        bmi = (float(weight) / float(height * height)) * 703
        print('BMI: ', bmi)
        print('(CDC: 18.6-24.9 normal)\n')
    except:
        print('Could not calculate health info.\n')
    user_input = input("Enter any key ('q' to quit): ")

try:
    number1 = int(input())
    print(number1 * 2)

    number2 = int(input())
    print(number2 * 2)
except:
    print('x')
print('e')


try:
    number1 = int(input())
    print(number1 * 2)

    number2 = int(input())
    print(number2 * 2)
except:
    print('x')
print('e')
user_input = input()
while user_input != 'q':
    try:
        number = int(user_input)
        print(number * 2)
    except:
        print('x')
    user_input = input()
print('e')

user_input = input()
while user_input != 'q':
    try:
        number = int(user_input)
        print(number * 2)
    except:
        print('x')
    user_input = input()
print('e')
user_input = input()
try:
    while user_input != 'q':
        number = int(user_input)
        print(number * 4)
        user_input = input()
except:
    print('x')
print('e')

#  Multiple exception handlers

user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        # Possible ZeroDivisionError
        print(60 // divisor) # Truncates to an integer
    except ValueError:
        print('v')
    except ZeroDivisionError:
        print('z')
    user_input = input()
print('OK')

numbers = [2, 4, 5, 8]
user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor > 20:
            # Possible NameError
            # compute() is not defined
            result = compute(result)
        elif divisor < 0:
            # Possible IndexError
            result = numbers[divisor]
        else:
            # Possible ZeroDivisionError
            result = 20 // divisor          # // truncates to an integer
        print(result, end=' ')
    except (ValueError, ZeroDivisionError):
        print('r', end=' ')
    except (NameError, IndexError):
        print('s', end=' ')
    user_input = input()
print('OK')


user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor < 0:
            # Possible NameError
            # compute() is not defined
            print(compute(divisor), end=' ')
        else:
            # Possible ZeroDivisionError
            print(20 // divisor, end=' ')     # // truncates to an integer
    except ValueError:
        print('v', end=' ')
    except ZeroDivisionError:
        print('z', end=' ')
    except:
        print('x', end=' ')
    user_input = input()
print('OK')

# Raising exceptions

#  BMI example with error-checking code that raises exceptions.

user_input = ""
while user_input != 'q':
    try:
        weight = int(input())
        if weight < 0:
            raise ValueError("Invalid weight.")
        height = int(input())
        if height <= 0:
            raise ValueError("Invalid height")
        bmi = (float(weight) * 703) / (float(height * height))
        print("BMI: ", bmi)
        print('(CDC: 18.6-24.9 normal)\n')
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')
    user_input = input("'q' to quite: ")


try:
    user_age = int(input())
    if user_age < 0:
        raise ValueError('Invalid age')
    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age
    print('Avg:', avg_max_heart_rate)

except ValueError as excpt:
    print(f'Error: {excpt}')

try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError('Invalid age')

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print('Avg:', avg_max_heart_rate)

except ValueError as excpt:
    print(f'Error: {excpt}')

valid_password = False

while valid_password == False:
    try:
        password = input()

        if len(password) < 8:
            raise ValueError('Invalid')

        valid_password = True
        print('Accepted')

    except ValueError as excpt:
        print(f'Error: {excpt}')

valid_password = False

while valid_password == False:
    try:
        password = input()

        if len(password) < 8:
            raise ValueError('Invalid')

        valid_password = True
        print('Accepted')

    except ValueError as excpt:
        print(f'Error: {excpt}')

#  ------------- BMI example using exception-handling constructs along with functions.-------------

def get_weight():
    weight = int(input())
    if weight < 0:
        raise ValueError("Invalid weight.")
    return weight

def get_height():
    height = int(input())
    if height <= 0:
        raise ValueError("Invalid height.")
    return height

user_input = ""
while user_input != 'q':
    try:
        weight = get_weight()
        height = get_height()
        bmi = (float(weight)/ float(height * height)) * 703
        print("BMI: ", bmi)
        print('(CDC: 18.6-24.9 normal)\n')
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate health info.\n")
    user_input = input('q to quite')


#  Using finally to clean up

nums = []
rd_nums = -1
my_file = input('Enter file name: ')

try:
    print('Opening', my_file)
    rd_nums = open(my_file, 'r')  # Might cause IOError

    for line in rd_nums:
        nums.append(int(line))  # Might cause ValueError
except IOError:
    print('Could not find', my_file)
except ValueError:
    print('Could not read number from', my_file)
finally:
    print('Closing', my_file)
    if rd_nums != -1:
        rd_nums.close()
    print('Numbers found:', ' '.join([str(n) for n in nums]))

def divide(a, b):
    z = -1
    try:
        z = a / b
    except ZeroDivisionError:
        print('Cannot divide by zero')
    finally:
        print("Result is", z)
divide(4,0)
# divide(4,2)


#  Fat burning heart rate
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    return 0.7 * (220-age)

    # return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {heart_rate:.1f} bpm")
    
    except ValueError as ve:
        print(f"{ve}\nCould not calculate heart rate info.")

    #  Exception handling to detect input string vs. integer
parts = input().split()
name = parts[0]
while name !='-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0
    print(f"{name} {age}")

    parts = input().split()
    name = parts[0]

# Exceptions with lists

names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']

while True:
    try:
        index = int(input("Enter an index (0 - 9): "))
        print(f'Name: {names[index]}')
        break  # Exit the loop on successful input

    except IndexError:
        print("Exception! list index out of range")  # Specific error message
        closest_name = names[0] if index < 0 else names[-1]
        print(f"The closest name is: {closest_name}")  # No 'valid' notion
"""
