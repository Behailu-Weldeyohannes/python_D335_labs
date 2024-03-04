"""
#  Assign variables, mathematical operations
#  Output the total distance traveled to two decimal places
travels = {
    "Employee A":int(input()),
    "Employee B":int(input()),
    "Employee C":int(input())
}

commute = {"Employee A": 15.62,
       "Employee B": 41.85,
       "Employee C": 32.67
       }

total_distance = 0


for employee in travels:
    dis_traveled = travels[employee]
    emp_commute = commute[employee]
    total_distance += dis_traveled * emp_commute
print(f"Distance: {total_distance:.2f} miles")
#  Assign variables, modulus operator (%)




"""
# Assign variables, modulus operator (%)












