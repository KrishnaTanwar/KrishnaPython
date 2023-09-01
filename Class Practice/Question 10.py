# Question 10: Program to calculate Volume of cylinder.

# Input Section
import math

a = int(input("Enter the radius of Cylinder:"))
b = int(input("Enter the height of Cylinder:"))

# Logic Section

vol = (math.pi)*a**2*b

# Output Section

print("The Volume of given Cylinder with radius",a," and height",b,"is",vol)
