# Question 1: Write a program that converts a given number of days into weeks and days.

# Input Section

a = int(input("Enter the no. of days:"))

# Logic Section

lg1 = a//7
lg2 = a - lg1*7

# Output Section

print("The no. of weeks",lg1,"and remaining days are",lg2,'Question 1.py')
