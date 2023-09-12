# Ques 1: Input 2 integers and a threshold k. find the maximum value between bitwise and(&), or(|) and xor(^). The maximum should not greater than the thershold k. The default maximum value is zero.

# Input Section

a,b = input().split()
a = int(a)
b = int(b)
k = int(input())


# Logic Section

r1 = a & b
r2 = a | b
r3 = a ^ b

r1 = r1*(r1<k)
r2 = r2*(r2<k)
r3 = r3*(r3<k)

out = max(r1,r2,r3)

#Output Section
print(out)
    
