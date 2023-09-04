# Checking for Leap Year.

# Input Section

yr = int(input("Enter an year: "))

# Logic Section

if yr%400==0:
    print("Leap Year")
else:
    if yr%4==0:
        if yr%100!=0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Not a Leap Year")
