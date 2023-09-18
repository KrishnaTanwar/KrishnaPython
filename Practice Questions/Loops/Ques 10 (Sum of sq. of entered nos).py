# Ques 10 : Program that reads number until their sum is 0. Display sum of squares
# of all entered number. If 1st no is equal to 0. Print 0.

n = []
s=0 
sq = 0
a = None
if a==0:
    print("Sum of squares: 0")

else:
    while True:
        n.append(a)
        a = int(input("Value of a: "))
        sq += a**2
        s+=a
        if s==0:
            print("Sum of squares:",sq)
            break
