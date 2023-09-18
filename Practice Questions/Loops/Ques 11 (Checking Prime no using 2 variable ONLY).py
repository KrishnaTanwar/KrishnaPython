# Ques 11: Program to check whether given no is Prime or Not without using 3rd variable.

p = None
a = int(input("Enter a no. (except 1): "))
for i in range(2,(a//2)+1):
    if a%i==0:
        p = 'not'
    
if p=='not':
    print(a,'is Not  a prime no')
else:
    print(a,'is a Prime number')
