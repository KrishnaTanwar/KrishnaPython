# Logical Expressions For c = 1 output should be 100 and for c = 0 output should be 200 
a = 100
b = 200
c = int(input("Enter the value of c 1/0: "))
logic = a*c + b*(1-c)
print(logic)
