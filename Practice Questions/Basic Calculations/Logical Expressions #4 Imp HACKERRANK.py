# Using CEIL and FLOOR function without using built-in function with f-string:

# Input Section

a = eval(input('Enter number:'))

# Logic Section

ceil = -(-a//1)
floor = a//1

# Output Section

print("Ceil is:",f'{ceil:.6f}')
print("Floor is:",f'{floor:.6f}')
