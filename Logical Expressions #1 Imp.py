#Write a Python program that takes an integer num as input. If num is even, the program should output "Even Number." If num is odd, it should output "Odd Number.
num = int(input("Enter a number: "))
result = ("Odd Number", "Even Number")[num % 2 == 0]
print(result)
