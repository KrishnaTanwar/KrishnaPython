#Ques 9: Hypotenuse of a right Angled Triangle, Base, and height is given by the user.
import math
a = int(input("Enter the base length of Right Angled Triangle: "))
b = int(input("Enter the height length of Right Angled Triangle: "))

#Logic 1 using MATH Module
a2 = a**2
b2 = b**2
Hypo = math.sqrt(a2 + b2)

# Logic 2 using ** operator
Hypo = (a**2 + b**2)**0.5

#Output Section
print(Hypo)
