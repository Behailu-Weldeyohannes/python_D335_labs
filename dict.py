"""
# travels = {
#     "Employee A": int(input("Travels for Employee A: ")),
#     "Employee B": int(input("Travels for Employee B: ")),
#     "Employee C": int(input("Travels for Employee C: ")),
# }
# emp = {"Employee A": 15.62, "Employee B": 41.85, "Employee C": 32.67}
# emp_id = {1: 15.62, 2: 41.85, 3: 32.67}

#  print key
# print(travels["Employee A"])
# print(emp_id[2])

#  adding new items
# emp_id[4] = 46.8
# print(emp_id)
#  wiping out
# emp_id = {}
# print(emp_id)
#  looping through a dictionary

# for id in emp_id:
#     print(id)
#     print(emp_id[id])

# student_scores = {
#     "Alice": 95,
#     "Bob": 82,
#     "Charlie": 78,
#     "Diana": 91,
#     "Peter": 61
# }

#  create an empty dictionary called student_grade
# student_grades = {}
#  add grade to students_grade

# for s in student_scores:
#     score = student_scores[s]
#     if score >= 91:
#         student_grades[s] = "Outstanding"
#     elif  score >= 81:
#         student_grades[s] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[s] = "Acceptable"
#     else:
#         student_grades[s] = "Fail"
# print(student_grades)
# print(student_grades["Peter"])

#  nesting dict and list

department_a = {"salaries": 50000, "supplies": 1000, "utilities": 2000}
department_b = {"salaries": 60000, "supplies": 1200, "rent": 5000}

dict1 = {'key1': 10, 'key2': 5, 'key3': 3}
dict2 = {'key1': 4, 'key2': 2, 'key3': 6}

result = {}

for key in dict1:
    if key in dict2:
        result[key] = dict1[key] + dict2[key]
    else:
        result[key]= dict1[key]
# print("Addition:",result)
print(result[key])
"""
commute = {
    "Employee A": 15.62,
    "Employee B": 41.85,
    "Employee C": 32.67
    }
travels = {
    "Employee A": int(input()),
    "Employee B": int(input()),
    "Employee C": int(input())
    }

total_distance = 0

for employee in commute:
    commute_distance = commute[employee]
    travel_count = travels[employee]
    total_distance = total_distance + commute_distance  * travel_count
print(total_distance)



