# Sum of Even Number till UserEntered Number.

# CONCEPT USED

"""
RANGE CONCEPT:

 1. range(stop): Generates numbers from 0 up to (but not including) the specified 'stop' value.

 Example :   for i in range(5):
                print(i)  # Output: 0, 1, 2, 3, 4
     
2. range(start, stop): Generates numbers from 'start' up to (but not including) the specified 'stop' value.
     
Example :   for i in range(2, 5):
                print(i)  # Output: 2, 3, 4
     
3. range(start, stop, step): Generates numbers from 'start' up to (but not including) the specified 'stop' value, 
                             with a specified 'step' between numbers.
Example :   for i in range(1, 10, 2):
                print(i)  # Output: 1, 3, 5, 7, 9
"""

#NOTE:
#1. The 'stop' argument is REQUIRED, while 'start' and 'step' are OPTIONAL.
#2. If only one argument is provided, it is considered as 'stop', and the sequence starts from 0.

"""
FOR LOOP CONCEPT:
 
 1. It is like a chef going through a recipe one step at a time. 
 2. It helps Python go through a list, numbers, or any bunch of things, doing the same job for each one. 
 3. It's like saying, "For each item in this list, do something specific!"

Example:
  
  fruits = ["apple", "banana", "orange"]
    for fruit in fruits:
        print(fruit)

  Output:

  apple
  banana
  orange
"""

#NOTE:
#1. 'for variable in sequence:' is the basic structure.
#2. It's handy for doing repetitive tasks without writing the same code over and over.
 

# INPUT SECTION
num = int(input("Enter a number: "))

# LOGIC SECTION
 
sum = 0
for a in range(2, num + 1, 2): #(num+1)-1 = num
    sum += a #sum = sum + a

# OUTPUT SECTION
    
print(f"The sum of even numbers from 1 to {num} is: {sum}")
