# Question 1 : Program to find whether an entered number is prime or not.


# Input Section

a = int(input("Enter a number: "))
y = int(a/2)

# Logic Section

for x in (1,y):
    lg1 = a%x
if lg1==0:
    print(a," is NOT a Prime number.")
else:
    print(a,"is a Prime Number.")

