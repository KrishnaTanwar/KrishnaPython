'''A man has certain number of apples.
If he picks them in a group of 7, he can pick all of them.
If he picks them in a group of 6, 1 apple is left behind.
If he picks them in a group of 5, 1 apple is left behind.
If he picks them in a group of 4, 1 apple is left behind.
If he picks them in a group of 3, 1 apple is left behind.
If he picks them in a group of 2, 1 apple is left behind.
Write a program that identifies the minimum number of apples he has'''


# Input Section

apples = int(input("Total no. of apple:"))

# Logic Section

while True:
    if apples % 7 == 0 and apples % 6 == 1 and apples % 5 == 1 and apples % 4 == 1 and apples % 3 == 1 and apples % 2 == 1:
        break
    apples += 1

# Output Section

print("The minimum number of apples he has is:", apples)
