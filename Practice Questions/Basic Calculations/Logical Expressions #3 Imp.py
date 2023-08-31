# Checking Divisibility of a number by two divisors WITHOUT using if-else!

# Input Section

a = int(input('Enter the number:'))
d1 = int(input('Enter the 1st Divisor:'))
d2 = int(input('Enter the 2nd Divisor:'))

# Logic Section

lg1 = a%d1
lg2 = a%d2

chk = lg1==0 and lg2==0
out = 'Yes.'*chk + 'No.'*(1-chk)

# Output Section

print(out)
