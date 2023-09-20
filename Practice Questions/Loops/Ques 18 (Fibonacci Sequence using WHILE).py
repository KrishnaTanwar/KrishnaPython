# Ques 6 : Fibonacci Series (1+2+3+5+11+22+...)

# Input Section
n = int(input("Enter limit: "))

a = 0
b = 1

print(a, b,  end = " ")
while n>2:
    c = a+b
    print(c, end=' ')
    a,b=b,c
    n-=1
