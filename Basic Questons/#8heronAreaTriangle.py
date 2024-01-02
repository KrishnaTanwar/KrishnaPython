# Area of Triangle using HERON'S Formula

# CONCEPT USED

"""
1. Function Definition:

  Syntax: 'def function_name(parameters):'

  a. The 'def' keyword is used to define a function.
  b. 'function_name' is the name of the function.
  c. 'parameters' are input values that the function can accept (optional).
  d. A colon (':') indicates the start of the function body.

2. Function Body:
  a. Contains the code to be executed when the function is called.
  b. Indentation is crucial to define the scope of the function.

3. Return Statement:
  a. 'return' keyword is used to send a value back from the function.
  b. It specifies the result or output of the function.
  c. A function may not have a 'return' statement, or it can have multiple return statements.

4. Function Call:
  a. Invoked by using the function name followed by parentheses.
  b. Arguments (values or variables) can be passed to the function when calling it.

5. Example: Adding Two Numbers

  def addnumbers(a, b):
      sum = a + b
      return sum
      print(sum)

  result = addnumbers(5, 3) #8
  print(result) #8


6. Benefits of Functions:
  a. Encapsulation: Groups related code together.
  b. Reusability: Functions can be called multiple times.
  c. Readability: Breaks down complex tasks into smaller, more understandable parts.
  d. Modularity: Allows for the organization of code into manageable components.
  
"""

## MAIN BODY ##

# INPUT SECTION

x = float(input("Enter the length of side a: "))
y = float(input("Enter the length of side b: "))
z = float(input("Enter the length of side c: "))

# LOGIC SECTION

# FUNCTION DEFINITION

def area(a, b, c):
    # Calculate semi-perimeter
    s = (a + b + c) / 2

    # Calculate area using Heron's formula
    Harea = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    return Harea

triArea = area(x, y, z)

# OUTPUT SECTION

print(f"The area of the triangle Using HERON's Formula with sides {x}, {y}, and {z} is: {triArea:.2f}")
