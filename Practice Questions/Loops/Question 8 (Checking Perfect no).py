# Question 8: Check whether given number is perfect or not.

#Input Section

a = int(input("Enter a no.: "))
s = 0

#Logic Section

for i in range(1,a):
    if a%i==0:
        s+=i

if s==a:
    print("Perfect no.")
else:
    print("Non-perfect no.")



#Output Section

print("Sum of divisors",s)
