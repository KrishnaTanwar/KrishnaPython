# Function to convert days to weeks and days

def daystoweekdays(days):
    # Calculate the number of weeks using integer division
    weeks = days // 7 #15//7 = 2
    
    # Calculate the remaining days after converting to weeks using modulous
    remaining_days = days % 7 #15%7 = 1
    
    # Display the result in a user-friendly format
    print(f"{days} days is equal to {weeks} weeks and {remaining_days} days.")

# Get input from the user
day = int(input("Enter the number of days: "))

# Call the function with the user input
daystoweekdays(day)
