'''Program Underflow, Full and Overflow of a cylindrical tank with r = 5m and h = 10m. The rate of flow is 15 m^3 / minute. Also, calculate the height of water left in container. Time to on the pump is given by user in minutes'''

#Input Section

t = eval(input("Enter time for the pump to be on (in min): "))
h= 10
r = 5
v = 3.14*5**2*10

# Logic Section

if t*15<v:
    print("Underflow","Volume left",v-15*t)
    ht = (v-15*t)/(3.14*5**2)
    hr= h-ht
    print(f"Filled height {ht:.2f}\n Remianing {hr:.2f}")
elif t*15 ==v:
    print("FULL")
else:
    print("Overflow")
    print("Volume of falling water",15*t-v)
