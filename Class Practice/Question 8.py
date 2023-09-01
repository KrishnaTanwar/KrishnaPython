# Question 8: Program to calculate area of triangle using HERON's Formula.

# Input Section

a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))

# Logic Section

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5

# Output Section

print("The Area of given triangle with sides",a,b,"and",c,"is",area)
