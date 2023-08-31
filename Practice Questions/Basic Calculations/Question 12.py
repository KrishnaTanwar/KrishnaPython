#Ques 12 : Program to find whether a triangle is scalene, isosceles, right angled or invalid when the sides of the triangle are entered by the user

# Input Section
a = int(input("Enter the 1st side of triangle: "))
b = int(input("Enter the 2nd side of triangle: "))
c = int(input("Enter the 3rd side of triangle: "))

#Logic Section & Ouput Section

if a + b <=c or b + c <=a or c + a <=b:
    print("Invalid data. This is NOT a triangle.")
elif a==b==c:
    print("Given Triangle with sides",a,b,c,"is a EQUILATERAL Triangle.")
elif a==b or b==c or a==c:
    print("Given Triangle with sides",a,b,c,"is a ISOCELES Triangle.")
elif a**2==b**2+c**2 or b**2==c**2+a**2 or c**2==b**2+a**2:
    print("Given Triangle with sides",a,b,c,"is a RIGHT ANGLED Triangle.")
else:
    print("Given Triangle with sides",a,b,c,"is a SCALENE Triangle.")
print("Thankyou!")
    
        
    
