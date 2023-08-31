# Question 2: Program to input two numbers and subtract the smaller number from the greater number.

# Input Section

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

# Logic Section

if a<b:
    print("The subtraction of",a,'and',b,'is',b-a)
else:
    print("The subtraction of",a,'and',b,'is',a-b)
