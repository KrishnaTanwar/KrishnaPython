#Ques 1: Program that takes an integer input from user
#and counts down from that number to 1 using while loop.

# Input Section

import time
a = int(input("Enter a no: "))
print("Counter Start")
while a>=1:
    print(a)
    a -=1
    time.sleep(0.5)
print("Counter Stop")
