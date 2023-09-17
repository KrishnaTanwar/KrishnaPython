#Ques 4 : Write the program to create building structure like the burj khaleefa with equivalent binary numbers



# Input Section
n = int(input())
w = len(bin(n)[2:])
for i in range(n+1):
    i = bin(i)
    j = i[2:]
    print(f'{j:>{w}}')
