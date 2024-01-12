#Ques 1:  Even Odd Checking WITHOUT using if-else statement

# INPUT SECTION

num = int(input("Enter a number: ")) #5

# LOGIC SECTION

res = num % 2 # TRUE(1)/FALSE(0)  # 1
out = 'ODD' * res + 'EVEN' * (1 - res) # 'ODD'*1 + 0 = 'ODD'

# OUTPUT SECTION

print(out) #ODD