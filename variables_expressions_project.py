
# *************Variables and Expressions*************
# Mathematical operation: time converter

h = int(input())
m = int(input())
s = int(input())

total_s =  (h * 3600) + (m * 60) + s
print(f"Seconds: {total_s}") 


# convert to seconds
seconds = int(input())

h = seconds // 3600
m = (seconds % 3600) // 60
s = seconds % 60

print(f"{h}\n{m}\n{s}")

#  Pizza party using math function 
import math
num_people = int(input())
cost = 14.95
total_slice = num_people * 2
slices_per_pizza = 12

total_pizzas = math.ceil(total_slice /slices_per_pizza)
total_cost = total_pizzas * cost
print(f"Pizzas: {total_pizzas}")
print(f"Cost: ${total_cost:.2f}")

# hypotenuse
import math
leg_a = float(input()) 
leg_b = float(input())

# hypotenuse = math.sqrt(leg_a**2 + leg_b**2)
hypotenuse = (leg_a**2 + leg_b**2) ** 0.5
print(f"Hypotenuse: {hypotenuse:.2f}")

#  area of triangle
import math
side_a = float(input())
side_b = float(input())
side_c = float(input())

s = (side_a + side_b + side_c) / 2
area = math.sqrt(s *(s-side_a) *(s-side_b) * (s - side_c))

print(f"The area of the triangle is: {area:.3f}")

#  ordering pizza
num_pizza = int(input())
cost = 9.99
tax = 0.06
sub_total = num_pizza * cost
total = (sub_total * tax) + sub_total
print(f"Subtotal: ${sub_total:.2f}\nTotal due: ${total:.2f}")

#  square root
import math
user_input = float(input())
result = math.sqrt(user_input)
print(f"Sqrt: {result:.2f}")

#  volume and area cylinder
import math
radius = float(input())
height = float(input())
volume = math.pi * pow(radius, 2) * height
area = 2 * math.pi * radius * height + 2 * math.pi * pow(radius, 2)

print(f"Vloume: {volume:.1f} cubic inches")
print(f"Surface area: {area:.1f} square inches")


# variables, input, and type conversions

user_int = int(input("Enter integer (32 - 126):\n"))
user_float = float(input("Enter float:\n"))
user_char = input("Enter character:\n")[0]
user_str = str(input("Enter string:\n"))
print(f"{user_int} {user_float} {user_char} {user_str}")
#  reverse order
# print(f"{user_str[::-1]} {user_char} {user_float} {user_int}")
print(f"{user_str} {user_char} {user_float} {user_int}")
int_to_char = chr(user_int)
print(f"{user_int} {user_float} {user_char} {user_str} {user_int} converted to a character is {int_to_char}")

#  cooking measurement converter
num_lemon_cup = float(input("Enter amount of lemon juice (in cups):\n"))
num_water_cup = float(input("Enter amount of water (in cups):\n"))
num_agave_cup = float(input("Enter amount of agave nectar (in cups):\n"))
num_serving = int(input("How many servings does this make?\n"))
total = num_lemon_cup + num_water_cup + num_agave_cup
print()

print(f"Lemonade ingredients - yields {num_serving:.2f} servings\n{num_lemon_cup:.2f} cup(s) lemon juice\n{num_water_cup:.2f} cup(s) water\n{num_agave_cup:.2f} cup(s) agave nectar")

num_serving = float(input("How many servings would you like to make?\n"))
num_lemon_cup = float(input("Enter amount of lemon juice (in cups):\n"))
num_water_cup = float(input("Enter amount of water (in cups):\n"))
num_agave_cup = float(input("Enter amount of agave nectar (in cups):\n"))
total = num_lemon_cup + num_water_cup + num_agave_cup
print()

print(f"Lemonade ingredients - yields {num_serving:.2f} servings\n{num_lemon_cup:.2f} cup(s) lemon juice\n{num_water_cup:.2f} cup(s) water\n{num_agave_cup:.2f} cup(s) agave nectar")

num_lemon_gallon = num_lemon_cup / 16
num_water_gallon = num_water_cup / 16
num_agave_gallons = num_agave_cup / 16
print(f"Lemonade ingredients - yields {num_serving:.2f} servings")
print(f"{num_lemon_gallon} gallon(s) lemon juice\n{num_water_gallon} gallon(s) water\n{num_agave_gallons} gallon(s) agave nectar")


#  food receipt
# item_name = input('Enter food item name:\n')

# FIXME (1): Finish reading item price and quantity, then output a receipt
food_item = input("Enter food item name:\n")
food_price = float(input("Enter item price:\n"))
item_quantity = int(input("Enter item quantity:\n"))
print()
print("RECEIPT")
receipt = item_quantity * food_price
print(f"{item_quantity} {food_item} @ ${food_price:.2f} = ${receipt:.2f}\nTotal cost: ${receipt:.2f}")
print()
print()
# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
food_item2 = input("Enter second food item name:\n")
food_price2 = float(input("Enter item price:\n"))
item_quantity2 = int(input("Enter item quantity:\n"))
print()
print("RECEIPT")
receipt2 = (item_quantity2 * food_price2) 
total_cost = receipt + receipt2
print(f"{item_quantity} {food_item} @ ${food_price:.2f} = ${receipt:.2f}")
print(f"{item_quantity2} {food_item2} @ ${food_price2:.2f} = ${receipt2:.2f}\nTotal cost: ${total_cost:.2f}")
print()
   
# FIXME (3): Add a gratuity and total with tip to the second receipt
gratuity = 0.15 * total_cost
total_with_tip = gratuity + total_cost
print(f"15% gratuity: ${gratuity:.2f}\nTotal with tip: ${total_with_tip:.2f}")