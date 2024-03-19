
#  ************** Chapt 34 *************
# 1. Assign variables, mathematical operations
# 2. Assign variables, modulus operator 

# 3. Formatted output of data type
           # ------- example 1:  phone number
phone_number = input("Enter your phone number: ")
while len(phone_number) == 10 and phone_number.startswith('0'):
    print("Phone number should not start with 0. Please re-enter.")
    phone_number = input("Enter your phone number: ")
country_code = input("Enter your country code: ")
formatted_number = f'+{country_code} {phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}'
print('Formatted phone number:', formatted_number)

# 4. Data types in formulas
# 5. Data type conversions
# 6. Convert integer to formatted string
# 7. Comparison operations with Boolean values
# 8. Try block with exception error
# 9. Branching conditional logic
# 10.Dictionary key search
# 11. Dictionary conditional logic
# 12. Manipulate text files
# 13. Manipulate CSV files
# 14. Math module
#15. Import custom module

#  ********** Chapter 33 **********






