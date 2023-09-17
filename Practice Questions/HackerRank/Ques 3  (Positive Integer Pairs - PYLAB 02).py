# Ques 3 : Write a program for the given integers P and X, that display the positive integer pairs (i, j) with satisfy the following conditions.
#i + j == P
#i XOR(^) j == X

# Input Section

p = int(input("P"))
x = int(input("X"))

for i in range(p//2+1):
    j = p - i
    if i^j == x:
        print("i , j",i,j)
