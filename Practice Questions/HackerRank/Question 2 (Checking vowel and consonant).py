# Q 2: This program will read a character from user and check whether it is VOWEL or CONSONANT if entered character was an alphabet using conditional opertors statement.

# Input Section

a = input("Enter a character (ONLY 1 CHARACTER): ")
b = a.isalpha()

# Logic Section

if b==True:
    if a in ('a','e','i','o','u') and ('A','E','I','O','U'):
        print("Vowel.")
    else:
        print("consonant.")
else:
    print("Not an Alphabet.")
    
