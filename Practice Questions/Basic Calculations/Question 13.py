# Ques 13: Find Simple Interest & total amount When Principal, Rate of Interest & time is entered by user.

#Input Section

p = int(input("Enter Principal amount: "))
r = int(input("Enter Rate of Interest (per annum): "))
t = int(input("Enter Time (in year): "))

#Logic Section

si = (p*r*t)/100

#Output Section

print("The Simple Interest is:",si)
