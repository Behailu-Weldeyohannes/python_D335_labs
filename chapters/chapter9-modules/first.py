import second

def one(number):
    return number - 5

def two(number):
    return number + 4

def three(number):
    return one(number) * two(number)

def four(number):
    return second.three(number)