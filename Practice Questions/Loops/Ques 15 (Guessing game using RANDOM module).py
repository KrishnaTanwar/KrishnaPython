# Ques 3 : Create a simple no. guessing game when computer selects a random no between 1 & 100, and
#the user has to guess it. Use a while to keep the game running until the user guesses correctly.

# Input

import random
c = 0
n = random.randrange(1,100)
score = 10
while True:
    a = int(input("Guess the number 1 to 100 "))
    if a == n:
        print("You win with score",score,)
        break
    elif a < n:
        print("Too Small")
        print(f"You have {score-1} chances remaining")
    else:
        print("Too Large")
        print(f"You have {score-1} chances remaining")
    score -=1
