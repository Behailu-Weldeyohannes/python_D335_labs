
#  ********* Chapter Ten: Files ********
"""

#  Reading files

# Creating a file object and reading text.

# print('Opening file my_file.txt.')
f = open('my_file.txt') #  create file object
# print('Reading file my_file.text')
contents = f.read() # read file text into a string
# print('Closing file my_file.txt')
f.close() # close the file
# print('\nContents of my_file.txt')
print(contents)
#  read up to 500 bytes
my_file = open('readme.txt')
contents = my_file.read(500)
my_file.close()

my_file = open('readme.txt')
lines = my_file.readlines()
print(lines[1])
my_file.close()
#  Calculating the average of data values stored in a file.
# Echo the contents of a file.
f = open('my_file.txt')

for line in f:
    print(line, end="")

f.close()

# Writing files
f = open('my_file.txt', 'w')  # Open file
f.write('Example string:\n  test....')  # Write string
f.close()  # Close the file
#  The write() method accepts a string argument only. Integers and floating-point values must first be converted using str(), as in f.write(str(5.75)).
#  file modes
a = open('myfile.txt', 'a') #  opens a file for writing
b = open('my_file.txt', 'w')#  overwrites the contents of an existing file or opens a new file for writing.
c = open('my_file.txt', 'a+') # The 'a+' mode opens the file for both reading and writing, appending new writes.

myfile = open('myfile.txt', 'w')
myfile.write('Num')
myfile.write('5')
myfile.write('\n')

#  the with statement

print('Opening myfile.txt')

try:
    # Open a file for reading and appending
    with open('myfile.txt', 'r+') as f:
        # Read in two lines
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        
        # Check if both lines are not empty
        if line1 and line2:
            num1 = int(line1)
            num2 = int(line2)
            product = num1 * num2
            # Move the file pointer to the end of the file
            f.seek(0, 2)
            # Write back result on a new line
            f.write('\n')
            f.write(str(product))
        else:
            print('Error: Empty lines in the file.')
except FileNotFoundError:
    print('Error: File not found.')

print('Closed myfile.txt')


#  Comma separated values file
import csv
with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')
    row_num = 1
    for row in grades_reader:
        print(f'Row #{row_num}: ', row)
        row_num += 1
#  Using csv file contents to perform calculations.
import csv

row1 = ['100', '50', '29']
row2 = ['76', '32', '330']

with open('gradeswr.csv', 'w') as csvfile:
    grades_writer = csv.writer(csvfile)
    grades_writer.writerow(row1)
    grades_writer.writerow(row2)
    grades_writer.writerows([row1], row2)

import csv
with open('myfile.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)

import csv
with open('myfile.csv', 'r') as myfile:
    csv_reader = csv.reader(myfile)
    for row in csv_reader:
        print(row[1])

#  Words in a range (lists)
file_name = input()
lower_bound = input()
upper_bound = input()

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error File not found.")
    exit()
#  strip newline characters from the lines and filter based on the search range
filtered_lines = [line.strip() for line in lines if lower_bound <= line.strip() <= upper_bound]
#  output the filtered lines
for line in filtered_lines:
    print(line)

#  Course Grade
# Get the input file name from the user
file_name = input()

# Read the student information from the TSV file
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: File not found.")
    exit()

# Initialize variables to store exam scores and counts
midterm1_total = 0
midterm2_total = 0
final_total = 0
num_students = 0

# Initialize a dictionary to store student information
students = {}

# Process each line in the TSV file
for line in lines:
    # Split the line into fields and extract student information
    fields = line.strip().split('\t')
    last_name, first_name = fields[:2]
    midterm1, midterm2, final = map(int, fields[2:])

    # Calculate average exam score
    avg_score = (midterm1 + midterm2 + final) / 3

    # Assign letter grade based on average score
    if avg_score >= 90:
        grade = 'A'
    elif avg_score >= 80:
        grade = 'B'
    elif avg_score >= 70:
        grade = 'C'
    elif avg_score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Update totals for average calculation
    midterm1_total += midterm1
    midterm2_total += midterm2
    final_total += final
    num_students += 1

    # Store student information in the dictionary
    students[(last_name, first_name)] = (midterm1, midterm2, final, grade)

# Calculate averages for each exam
avg_midterm1 = midterm1_total / num_students
avg_midterm2 = midterm2_total / num_students
avg_final = final_total / num_students

# Write student information and averages to report.txt
with open('report.txt', 'w') as report_file:
    for student, data in students.items():
        report_file.write(f"{student[0]}\t{student[1]}\t{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}\n")

    report_file.write(f"\nAverages: midterm1 {avg_midterm1:.2f}, midterm2 {avg_midterm2:.2f}, final {avg_final:.2f}\n")
    # print()

"""
