''' Question 17: Program to input the number of heads and feet in a farm and identify the number of chickens
and goats in the farm. For example, if there are 340 heads and 1,060 feet, there are 150
chickens and 190 goats.
'''

# Input Section

h = int(input("Enter the number of heads")) #100
f = int(input("Enter the number of feets")) #300

# Logic Section
# c + g = head
# 2c + 4g = feet

g = (f - 2*h)/2
c = h - g

# Ouput Section
print("There are",int(g),"goats and",int(c),"chikens.")

