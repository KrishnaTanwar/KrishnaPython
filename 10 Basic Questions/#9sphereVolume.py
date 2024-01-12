# Ques : Volume of Sphere

# CONCEPT USED

'''
# MATH MODULE: 

1. It provides access to a set of mathematical functions and constants.
2. It allows us to perform various mathematical operations beyond the basic arithmetic provided by the core language.

Example: Using 'math' Module to Calculate Square Root

import math
number = 25
sqroot = math.sqrt(number)
print(f"The square root of {number} is {sqroot}.")

Explanation:
1. The 'math.sqrt()' function is used to calculate the square root of the number 25.
2. The 'import math' statement is necessary to access functions and constants from the `math` module.
3. The 'sqrt()' function returns the square root of a given number, and the result is then printed.

'''

## MAIN CODE

#INPUT SECTION

radius = float(input("Enter the radius of the sphere (in m): "))

# LOGIC SECTION

import math
def sphereVolume(radius):
    volume = (4/3) * math.pi * radius**3 # 4/3*pie*r^3
    return volume

Vsphere = sphereVolume(radius) 

# OUTPUT SECTION

print(f"The volume of the sphere with radius {radius} is {Vsphere:.2f}.")
