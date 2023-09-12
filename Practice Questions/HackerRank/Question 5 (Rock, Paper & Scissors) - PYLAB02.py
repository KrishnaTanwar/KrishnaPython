#Ques 2 : Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Input Section

n1 = input()
n2 = input()

d1 = input()
d2 = input()

# Logic Section

if d1 == "Rock" and d2 == "Scissor":
    print(n1,"Win")
elif  d1 == "Scissor" and d2 == "Paper":
    print(n1,"Win")

elif d1 == "Paper" and d2 == "Rock":
    print(n1,"Win")

else:
    print(n2,'Win')
    
