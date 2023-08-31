# Checking a number whether it is even or odd and in a paricular range and then print 'Weird' and 'Not Weird'

# Input Section

a = int(input('Enter a number'))
les = int(input("Given number must less than:"))
grt = int(input("Given number must greater than:"))

# Logic Section

even = a%2
lg1 = even==0

rnge = a>les and a<grt
lg2 = rnge==0

out = lg2*('Weird'*lg1 + 'Not Weird'*(1- lg1))

# Output Section

print(out)
