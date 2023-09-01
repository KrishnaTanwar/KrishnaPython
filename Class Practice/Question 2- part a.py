# Question 2 part (a): Develop a temperature converter program that converts celsius to fahrenheit, and kelvin.

# Input Section

a = int(input("Enter temperature (in degree celcius):"))

# Logic Section

fh = a*(9/5)+32

kl = a + 273.15

# Output Section

print("Temperature in Degree Fahrenheit:", fh)
print("Temperature in Kelvin:", kl)
