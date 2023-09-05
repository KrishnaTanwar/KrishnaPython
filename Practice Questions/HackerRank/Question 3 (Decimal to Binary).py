# Q3: Read an integer number in Decimal and converts it into Binary Number System.

# Input Section

a = eval(input("Enter a number in Decimal number system: "))

# Logic Section

lg1 = str(a//2)
for x in lg1:
    if int(x)>=2:
        print(x/2)
        
