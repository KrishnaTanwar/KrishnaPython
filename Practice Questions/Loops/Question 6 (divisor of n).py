# Question 5 : Find divisors of given no.

#Input Section

a = int(input("Enter a no.: "))
d = []

#Logic Section

for i in range(1,a+1):
    if a%i==0:
        d.append(i)

#Output Section

print("Divisors are",d)
