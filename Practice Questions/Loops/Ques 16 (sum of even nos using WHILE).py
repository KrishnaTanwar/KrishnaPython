# Ques 4 : Sum of even numbers Using While Loop

# Input Section

a = int(input("Want Sum of Even numbers upto: "))
i = 1
s = 0
while i<=a:
    if i%2==0:
        s = s+i
    i +=1
print(s)
        
