# Question 6 : Find sum of divisors of given no.

#Input Section

a = int(input("Enter a no.: "))
s = 0

#Logic Section

for i in range(1,a+1):
    if a%i==0:
        s+=i

#Output Section

print("Sum of divisors",s)
