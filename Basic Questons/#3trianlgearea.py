#Calculation of Area of Right Angled Triangle

#INPUT SECTION

# Get input from the user
base = float(input("Enter the base of the triangle: "))  # Prompt user for the base and convert input to a float

height = float(input("Enter the height of the triangle: "))  # Prompt user for the height and convert input to a float

#LOGIC SECTION

# Calculate the area of the triangle
area = 0.5 * base * height  # Use the formula for the area of a triangle: 0.5 * base * height

# OUTPUT SECTION

# Display the result
print(f"The area of the triangle with base {base} and height {height} is: {area:.2f}")  # Print the calculated area with a user-friendly message
