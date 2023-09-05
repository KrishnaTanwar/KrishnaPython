# Question 8: Binary(base 2) to Octal(base 8) & Hexadecimal(base 16) Conversions

# Input Section

n = int(input("Enter a Binary number: "))

# Logic Section

lg2 = oct(n)
lg3 = hex(n)[2:]

# Output Section

print("Octal no. is",lg2)
print("Hexadecimal no. is",lg3)

