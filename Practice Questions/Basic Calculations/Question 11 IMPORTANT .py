# Ques 11: Program to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100),
#when the total number of currency notes counted altogether is minimum and there must be at
#least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user.

#Input Section

Amount = int(input("Enter the amount to be withdrawn: "))-100 #5200-100 = 5100

#Logic Section

two_k = Amount // 2000 #5100//2000 = 2
amount2k = Amount - two_k*2000 #5100-4000 = 1100

five_h = amount2k//500 #1100//500 = 2
amount5k = amount2k - five_h *500 #1100 - 1000 = 100

one_h = amount5k//100 #100//100 = 1
amount1h = amount5k - one_h*100 #100-100 = 0

#Output Section

print("No. of TWO Thousand notes are: ",two_k)
print("No. of FIVE Hindred notes are: ",five_h)
print("No. of ONE Hundred notes are: ",one_h + 1)
