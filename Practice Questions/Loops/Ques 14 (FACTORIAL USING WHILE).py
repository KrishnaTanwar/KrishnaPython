# Ques 2: Factorial using While Loop

# Input

n = int(input("Enter a no:"))
f = 1
while n>=1:
    f *=n
    n-=1
print(f'Factorial of given no {f}')
