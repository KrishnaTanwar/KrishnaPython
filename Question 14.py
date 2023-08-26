# Ques 14: Find Compound Interest & total amount When Principal, Rate of Interest & time is entered by user.

#Input Section

p = int(input("Enter Principal amount: "))
r = int(input("Enter Rate of Interest (per annum): "))
t = int(input("Enter Time (in year): "))
n = int(input("How many times you are investing (each year): "))

#Logic Section
 
ci = p*(1 + r/n)**n*t - p

#Output Section

print("The Compound Interest is (Annually):",ci)
