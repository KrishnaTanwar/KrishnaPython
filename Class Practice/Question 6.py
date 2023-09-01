# Question 6: Program to convert given number of seconds into hours, minutes and seconds.

# Input Section

a = int(input("Enter the number of seconds:"))

# Logic Section

hr = a//3600
a = a - hr*3600

mn = a//60
a = a - mn*60

sc = a

# Output Section

print("No. of seconds given by you can be represented as",hr,"Hours",mn,"Minutes and",sc,"seconds.")
