# Ques 3 : Write a Python program that takes user input for the values of a, b, and c (either 1 or 0). Depending on the value of c, the program should displays either the value of a or b.

# CONCEPT USED
'''

" ".format():

1. The '.format()' method in Python is used for string formatting.
2. It allows you to insert values into a string in a specified format.
3. It replaces placeholders in a string with values provided as arguments. 
4. It provides a flexible way to create dynamic strings by incorporating variables or expressions.

Example:

name = "Alice"
age = 25
message = "Hello, {}! You are {} years old.".format(name, age)
print(message) # Hello, Alice! You are 25 years old.
'''

# INPUT SECTION
a = 10
b = 20
c = int(input("Enter the value of c: 1 or 0: "))  # User input for the value of c

# LOGIC SECTION

# If c is 1, display the value of 'a'; otherwise, display the value of 'b'

result = a * c + b * (1 - c)

# OUTPUT SECTION

print("Value by choice is {0}".format(result))
