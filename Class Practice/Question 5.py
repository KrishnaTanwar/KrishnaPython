# Question 5: Program to find the greatest of 2 numbers.

# Input Section

a = int(input("Enter the first number(a):"))
b = int(input("Enter the second number(b):"))

# Logic Section

lg1 = a>b

lg = lg1*("a is greater than b.") + (1-lg1)*("b is greater than a.")

# Output Section

print(lg)
