# Question 2 part (c): Develop a temperature converter program that converts kelvin to celsius, fahrenheit, kelvin.

#Input Section

a = eval(input("Enter temperature (in kelvin):"))

# Logic Section

cl = a - 273.15

fh = cl * (9/5) + 32


# Output Section

print("Temperature in Degree Celcius:", cl)
print("Temperature in Degree Fahrenheit:", fh)
