# Function to convert seconds to hours, minutes, and remaining seconds.

# Facts to be Known:

"""

1 hour = 60 Minutes = 3600 Seconds
1 Minute = 60 Seconds

""" 

# Operators & Methods Used:

"""

1. Integer Floor Division (//): Quotient Value after division

The '//' operator performs integer division, discarding the remainder.

Example:
     result = 10 // 3
     print(result)  # Output: 3
     

2. Modulous Operator (%): Remainder after division

The '%' operator returns the remainder after division.

Example:
     remainder = 17 % 5
     print(remainder)  # Output: 2
     
3. F-string (Formatted String): 

It lets you to put VARIABLES or EXPRESSIONS directly into a STRING for Simplicity and Readability.

Example:
     name = "krishna"
     age = 19
     greeting = f"Hello, {name}! You are {age} years old."
     print(greeting) # Hello, Krishna! You are 19 years old.
"""

# Function Definition Section

def timeconverter(seconds): #7500
    hours = seconds // 3600  # 2
    minutes = (seconds % 3600)//60 #300//60 = 5
    remainingSeconds = seconds % 60 # 7500%60 = 0
    return f"{seconds} seconds is equal to {hours} hours, {minutes} minutes, and {remainingSeconds} seconds." 


# MAIN BODY
    
# INPUT SECTION
    
second = int(input("Enter the number of seconds: "))  #7500

# LOGIC SECTION

result = timeconverter(second) #7500

# OUTPUT SECTION

print(result)
