# Ques 5 : Password Validator using While Loop

# Input Section

a = input("Enter Password: ")
pswd = "Krishna123"
c = 0

while True:
    if a == pswd:
        print("Right Password")
        break
    else:
        print("Wrong Password \n Try Again")
        a = input("Enter password again: ")
        c+=1
        if c==5:
            print('Timed Out')
            break
