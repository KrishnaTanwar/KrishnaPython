# Question 2 part (b): Develop a temperature converter program that converts fahrenheit to celsius,and kelvin.

# Input Section

a = eval(input("Enter temperature (in degree Fahrenheit):"))

# Logic Section

cl = (a - 32)*(5/9)

kl = cl + 273.15

# Output Section

print("Temperature in Degree Celcius:", cl)
print("Temperature in Kelvin:", kl)
