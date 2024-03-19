#  ***********Python Cheat Sheet **************

# --- multiple variable declaration ---

var1, var2, var3 = 1,2,3
print(var3)

# --- Data Types ---
my_float = 13.0
dataType = type(my_float) # determines data type/class of object

convInt = int(my_float) # converts float to an integer
my_integer = 10

convFloat = float(my_integer) # converts integer to a float

convString = str(my_integer) # converts integer to string

print(round(4.8)) # rounds a float value to the nearest whole number

print(var1) # print command

# --- arithmetic operators ---
print( 2 + 2 )# addition

print( 2 - 2 ) # subtraction

print( 2 * 2 ) # multiplications

print( 2.1 / 2 ) # division, always results in float: 2.1 / 2 evaluates to 1.05

print( 2.1 // 2 ) # floor divisiion, gives the result of the last even division. Result will be a "mathematical integer" but whether it's a Python int or float depends on numbers used. 2.1 // 2 evaluates to  the float 1.0, while 5 // 2 evaluates to int 2

print( 5 % 2 ) # modulo (integer remainder), 5 % 2 evaluates to 1 (that's the 1 left over to get to 5 after 2 went into 4 evenly... see how floor division and modulo pair so well... 5 // 2 = 2, 5 % 2 = 1)

print( 2 ** 2 ) # power of.. 2**2 evaluates to 4

# --- assignment/reassignment operators ---

myNum = 10 # assignment

myNum += 5 # "add and"... adds to previous value

myNum -= 5 # "substract and"... subtract from previous value

myNum *= 5 # "multiply and"... multiply by previous value 

myNum /= 5 # "divide and"... divide by previous value

# --- comparison operators ---

myNum = print( myNum < 2 ) # less than

print( myNum > 2 ) # greater than

print( myNum <= 4 ) # less than or equal to

print( myNum >= 2 ) # greater than or equal to

print( myNum == 2 ) # equal to print( myNum != 2 ) # not equal to
