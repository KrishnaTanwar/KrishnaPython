# Question 4: Program to check eligibility of a person to vote(18) or not.

# Input Section

a = int(input("Enter Your age:"))

# Logic Section

lg = a>=18 
chk =("You can Vote") *lg + ("You can't vote ")*(1-lg)

# Output Section
print(chk)

