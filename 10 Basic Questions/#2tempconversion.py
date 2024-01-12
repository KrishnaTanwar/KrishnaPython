#Temperature Converter among Celcius, Fahrenheit and Kelvin.

# Get input from the user
temp = float(input("Enter the temperature: ")) #50
unit_from = input("From unit (C, F, K): ").upper() #c
unit_to = input("To unit (C, F, K): ").upper() #f/k

# Conversion logic
if unit_from == 'C' and unit_to == 'F':
    result = (temp * 9/5) + 32  # f = (9/5)C + 32
elif unit_from == 'C' and unit_to == 'K':
    result = temp + 273.15 # k = C + 273.15
elif unit_from == 'F' and unit_to == 'C':
    result = (temp - 32) * 5/9
elif unit_from == 'F' and unit_to == 'K':
    result = (temp - 32) * 5/9 + 273.15
elif unit_from == 'K' and unit_to == 'C':
    result = temp - 273.15
elif unit_from == 'K' and unit_to == 'F':
    result = (temp - 273.15) * 9/5
else:
    result = temp  # No conversion needed for the same units

# Display the result
print(f"{temp} {unit_from} is equal to {result:.2f} {unit_to}.") #50 C is equal to 234.00 F.
