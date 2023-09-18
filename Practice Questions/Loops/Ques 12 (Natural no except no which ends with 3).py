# Ques : Natural no. except number which ends with 3.

# Input Section
a = int(input("Enter upto no"))
for i in range(1,a):
    if i%10!=3:
        print(i,end=" ")
    else:
        print()
