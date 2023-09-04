#Question 2: Program to find the factorial of an entered number.

#Input Section
import math

a = int(input("Enter a number:"))

# Logic & Output Section

if a<0:
    print("Please enter a number greater than or equal to ZERO.")
elif a==0:
    print("Factorial of Zero (0!) is 1.")
else:
    print("Factorial of",a,"is",math.factorial(a))
