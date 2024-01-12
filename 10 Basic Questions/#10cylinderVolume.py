# Ques 10 : Volume of Sphere

# CONCEPT USED

'''

## 1. Exponentiation ('**') Operator: ## 

Used for exponentiation, meaning raising a number to the power of another. 

For example, 'a ** b' represents "a to the power of b or a^b."

PYTHON EXAMPLE:

result = 2 ** 3  # 2 raised to the power of 3
print(result)   # Output: 8

In the given example, '2 ** 3' calculates 2 raised to the power of 3, resulting in 8.

## 2. 'float()' Datatype: ## 

Used to convert a number or a string containing a number to a floating-point number (decimal number).

It is particularly useful when you want to ensure that a number is treated as a floating-point value.

PYTHON EXAMPLE:

str = "3.14"
flonum = float(str) # EXPLICIT TYPE CASTING
print(flonum)  # Output: 3.14


Here, 'float(str)' converts the string "3.14" to a floating-point number, 
and the result is stored in the variable 'flonum'.

'''

## MAIN CODE

# INPUT SECTION

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# LOGIC SECTION

# FUNCTION DEFINITION

def cylinderVolume(radius, height):
    pi = 3.14159  # Approximate value of pi
    volume = pi * radius**2 * height #pi*r^2*h
    return volume


# FUNCTION CALLING

cVolume = cylinderVolume(radius, height)

# OUTPUT SECTION

print(f'The volume of the cylinder with radius {radius} and height {height} is: {cVolume:.2f} cubic units.')
