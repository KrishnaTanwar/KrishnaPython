# Question 7: Decimal(base 10) to Binary(base 2), Octal(base 8) & Hexadecimal(base 16) Conversions

# Input Section

n = int(input("Enter a Decimal number: "))

# Logic Section

lg1 = bin(n)[2:]
lg2 = oct(n)
lg3 = hex(n)[2:]
# Output Section

print("Binary no. is",lg1)
print("Octal no. is",lg2)
print("Hexadecimal no. is",lg3)

