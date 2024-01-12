# Ques2: Develop a Python program to check if a given year is a leap year or not. Avoid using conventional if-else statements.

# CONCEPT USED
"""
1. '=' (Assignment Operator):

- The '=' operator is used for assignment in Python.
- It assigns the value on the right side to the variable on the left side.
  
Example:
  x = 5  # Assigns the value 5 to the variable x


2. '==' (Equality Operator):

- The '==' operator is used to check if two values are equal.
- It returns 'True' if the values are equal; otherwise, it returns 'False'.

Example:
  a = 10
  b = 5
  result = (a == b)  # Checks if a is equal to b, result will be False


3. '!=' (Not Equal Operator):

- The '!=' operator is used to check if two values are not equal.
- It returns 'True' if the values are not equal; otherwise, it returns 'False'.

Example:
  a = 10
  b = 5
  result = (a != b)  # Checks if a is not equal to b, result will be True

4. '%' (Modulo Operator):

- The '%' operator is the modulo operator, which returns the remainder of the division of the left operand by the right operand.

Example:
  x = 10 % 3  # Calculates the remainder of the division of 10 by 3, x will be 1.
"""

# INPUT SECTION

year = int(input("Enter a year: ")) # 240, 440

# LOGIC SECTION

# Use boolean expression to check if it's a leap year without using if-else
# The expression evaluates to True for leap years and False for non-leap years

res = year % 4 == 0 and year % 100 != 0 or year % 400 == 0 #True == 1

# Create a string based on the boolean result
# If res is True, it multiplies 'LEAP YEAR' by 1, otherwise, it multiplies 'NOT LEAP YEAR' by 0

out = 'LEAP YEAR' * res + 'NOT LEAP YEAR' * (1 - res) #'LEAP YEAR'

# OUTPUT SECTION

print(out)
