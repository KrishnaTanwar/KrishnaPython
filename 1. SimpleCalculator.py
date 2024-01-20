'''
1. Problem: Calculator
Description: Create a simple calculator class that can perform basic arithmetic operations
(addition, subtraction, multiplication, division).
'''

# CONCEPT USED
'''
1. Class and Object:

a. Class:

- Definition: A class is a blueprint or template for creating objects in Python.
   
- Purpose: It defines a set of attributes and methods that will be common to all objects created from the class.
   
- Example:
  
     class Dog:
         def __init__(self, name, age):
             self.name = name
             self.age = age
         
         def bark(self):
             print("Woof!")

------------------------------------------------------------------------------------------------------------
     
b. Object:

- Definition: An object is an instance of a class, representing a real-world entity.
   
- Purpose: Objects encapsulate data (attributes) and behaviors (methods) defined by the class.
   
- Example:

# Creating objects (instances) of the Dog class
     dog1 = Dog("Buddy", 3)
     dog2 = Dog("Max", 2)
     
# Accessing attributes and invoking methods of objects
     print(dog1.name)  # Output: Buddy
     dog2.bark()       # Output: Woof!
   

In summary, a class is like a blueprint that defines the structure and behavior, and an object is an instance of that blueprint, representing a specific entity with its own set of attributes and behaviors. The class provides a way to create objects with consistent properties and actions.

____________________________________________________________________________________________________________


2. Methods:

In Python, a method is a function that is associated with an object. It defines the behavior of the object and performs actions or computations. Methods are called on objects and can access and modify the object's attributes.

Example:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")

# Creating a Dog object
my_dog = Dog("Buddy", 3)

# Calling methods on the Dog object
my_dog.bark()               # Output: Buddy says Woof!
my_dog.celebrate_birthday() # Output: Buddy is now 4 years old.

In this example, the 'Dog' class has two methods, 'bark' and 'celebrate_birthday'. The 'bark' method prints a message, and the 'celebrate_birthday' method increments the dog's age and prints a birthday message. These methods are invoked on a 'Dog' object ('my_dog') to perform specific actions related to that object.

____________________________________________________________________________________________________________
'''

# MAIN CODE or DRIVER CODE

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"

# Example Usage:
        
calculator = Calculator()
a = int(input("Enter 1st number: "))
b = int(input(f"Enter 2nd number (<{a}): "))

result_add = calculator.add(a, b)
print("Addition:", result_add)

result_subtract = calculator.subtract(a, b)
print("Subtraction:", result_subtract)

result_multiply = calculator.multiply(a, b)
print("Multiplication:", result_multiply)

result_divide = calculator.divide(a, b)
print("Division:", result_divide)

'''
____________________________________________________________________________________________________________
____________________________________________________________________________________________________________
'''
