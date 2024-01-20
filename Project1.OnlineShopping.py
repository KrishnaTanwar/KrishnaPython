# Project 1: ONLINE SHOPPING #

# Write a Python program that simulates an item purchase scenario. The program displays available items, allows a user to demand specific quantities, calculates the total bill, and displays the user's cart and relevant details.

'''--------------------------------------------------------------------------------'''

# Episode 0: CONCEPT USED

"""
1. '\t': ESCAPE SEQUENCE

- In Python, '\t' is an escape sequence representing a horizontal tab. 
- When used in a string, it inserts a tab character, creating space equivalent to a tab key press.

- Example:

Input :

print("Hello\tWorld")

Output :

Hello   World


- Explanation: 
  
  In the above example, the '\t' inserts a tab space between "Hello" and "World," resulting in the words being separated by multiple spaces. This is commonly used for formatting and alignment in text output.


--------------------------------------------------------------------------------------

2. '<' or '>' Alignments in f-string:

- In Python f-strings, you can control the alignment of variables within a specified width using the '<' (left alignment) and '>' (right alignment) characters.

-- Left Alignment ('<'):

variable = "Hello"
formatted_text = f"({variable:<10}ji)"
print(formatted_text)

Output:
(Hello     ji)


In the example, the value of the variable is left-aligned within a field of width 10, with additional spaces added to the right before 'ji'.

-- Right Alignment ('>'):

variable = "Hi"
formatted_text = f"(Hello{variable:>10})"
print(formatted_text)

Output:

(Hello        Hi)


In this case, the value is right-aligned within a field of width 10, with spaces added to the left.

--------------------------------------------------------------------------------------

3. dictionary.items() : Dictionary Key-Value Pairs

-- In Python, 'dictionary_name.items()' is a method that returns a view object that displays a list of a dictionary's key-value tuple pairs. 

-- This provides a convenient way to iterate over both keys and values in a dictionary.

-- Example:

myDict = {'a': 1, 'b': 2, 'c': 3}

# Using dict.items() to iterate over key-value pairs

for key, value in myDict.items():
    print(f"Key: {key}, Value: {value}")

Output:

Key: a, Value: 1
Key: b, Value: 2
Key: c, Value: 3


In this example, 'dict.items()' allows you to iterate over key-value pairs in the 'myDict' dictionary, making it easy to work with both keys and values simultaneously in a loop.

--------------------------------------------------------------------------------------

4.dictionary.copy(): Making copy of a Dictionary

-- In Python, the 'dictionary.copy()' method is used to create a SHALLOW COPY of a dictionary. 
-- This means it produces a new dictionary with the same key-value pairs, but changes to the new dictionary won't affect the original, and vice versa.

-- Example:
    
originalDict = {'a': 1, 'b': 2, 'c': 3}

# Creating a shallow copy using dictionary.copy()
copiedDict = originalDict.copy()

# Modifying the copied dictionary
copiedDict['d'] = 4

# Displaying both dictionaries
print("Original Dictionary:", originalDict)
print("Copied Dictionary:", copiedDict)

Output:

Original Dictionary: {'a': 1, 'b': 2, 'c': 3}
Copied Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


In this example, changes made to the 'copiedDict' do not affect the 'originalDict'. The 'dictionary.copy()' method is useful when you want to duplicate a dictionary for independent use.

--------------------------------------------------------------------------------------

5. dictionary.pop(key): Removes key-value pair using key

-- In Python, the 'dictionary.pop(key)' method is used to remove and return the value associated with the specified key in a dictionary. 
-- If the key is not found, it raises a KeyError (unless a default value is provided).

Example:

myDict = {'a': 1, 'b': 2, 'c': 3}

# Using dictionary.pop() to remove and return the value associated with the key 'b'
removedValue = myDict.pop('b')

# Displaying the modified dictionary and the removed value
print("Modified Dictionary:", myDict)
print("Removed Value:", removedValue)

Output:

Modified Dictionary: {'a': 1, 'c': 3}
Removed Value: 2


In this example, 'dictionary.pop('b')' removes the key-value pair with the key 'b' from 'myDict` and returns the removed value (2). The modified dictionary is then displayed without the 'b' key.
"""

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



# Episode 1: Introduction and Displaying Available Items

# Function to display available items

# def displayAvailableItems(dct):
#     # Display header for available items
#     print("\t\tAvailable Items:")
#     print(f"{'S.No.':<15}{'Item':<15}{'Quantity':<15}{'Cost/Item':<15}")

    # # Display each item's details
    # for index, row in dct.items():
    #     print(f"{index:<15}{row['Item']:<15}{row['Quantity']:<15}{row['Cost/Item']:<15}")

# Available items dictionary
availableItems = {
    1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5},
    2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35},
    3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
    4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
    5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}
}

# Display available items
# displayAvailableItems(availableItems)


# '''--------------------------------------------------------------------------------'''


# Episode 2: Taking User Demand

# Available items dictionary
availableItems = {
    1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5},
    2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35},
    3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
    4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
    5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}
}

# User demand for items
userDemand = {}
for index, row in availableItems.items():
    item_name = row['Item']
    quantity = int(input(f"Enter the quantity of {item_name}: "))
    userDemand[item_name] = quantity
print(userDemand)

# Display user demand
print("\nUser Demand:")
for item_name, quantity in userDemand.items():
    print(f"{item_name}: {quantity}")


'''--------------------------------------------------------------------------------'''

# Episode 3: Calculating Bill and Updating Stock


# Available items dictionary
availableItems = {
    1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5},
    2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35},
    3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
    4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
    5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}
}

# Calculate bill and update stock
bill = 0
userCart = availableItems.copy()

# Loop through user demand and available items
for item_name, quantity in userDemand.items():
    for j in availableItems.copy():
        if item_name == availableItems[j]['Item']:
            if quantity <= availableItems[j]['Quantity']:
                tp = quantity * availableItems[j]['Cost/Item']
                bill += tp
                availableItems[j]['Quantity'] -= quantity
                userCart[j]['Quantity'] = quantity
                userCart[j]['TotalCost'] = tp
            else:
                # Display message for insufficient stock
                print(f"Sorry, we don't have enough {item_name} in stock")
                userCart.pop(item_name)
                break

# Display user's cart and details
print("\nUser's Cart:")
for index, row in userCart.items():
    print(f"{row['Item']}: {row['Quantity']} units - Total Cost: {row['TotalCost']}")
print('Total Item Cost:', bill)


'''--------------------------------------------------------------------------------'''

# Episode 4: Calculating Total Bill with Delivery Charge

# Delivery details
name = input("\nEnter your name: ")
address = input('Enter your address: ')
distance = int(input("Enter the distance: "))
deliveryCharge = 30

# Calculate total bill with delivery charge
totalBill = bill + deliveryCharge

# Display total item cost and bill amount
print('\nTotal Item Cost:', bill)
print('Total Bill Amount = Total Amount + delivery charge:', totalBill)

'''--------------------------------------------------------------------------------'''

# Episode 5: Displaying Customer Details and Conclusion

# Customer details
customerDetails = {'Name': name, 'Address': address, 'Distance': distance, 'Delivery Charge': deliveryCharge, 'Bill': totalBill}

# Display customer details
print("\nCustomer Details:")
for key, value in customerDetails.items():
    print(f"{key}: {value}")

# Conclusion
print("\nThank you for using our service! We hope you enjoy your purchase.")

'''--------------------------------------------------------------------------------'''
'''--------------------------------------------------------------------------------'''