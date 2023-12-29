# Greatest of the Two Numbers

#INPUT SECTION

num1 = int(input("Enter the first number: ")) #5
num2 = int(input("Enter the second number: ")) #6

# LOGIC SECTION

#1. Using MAX() function

max1 = max(num1, num2) #6

#2. Using IF-ELSE Statement

if num1>num2:
    max2 = num1 
else:
    max2 = num2 #6

#3. Using OPERATORS (WITHOUT any FLOW CONTROL statement)
    
check = num1>num2 #5>6 = FALSE (0)
max3 = num1*(check) + num2*(1-check) # 5*(0) + 6*(1-0) = 6

# OUTPUT SECTION

print(f"The greater of the two numbers is USING MAX(): {max1}")
print(f"The greater of the two numbers is USING IF-ELSE: {max2}")
print(f"The greater of the two numbers is USING OPERATORS: {max3}")

