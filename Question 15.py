#Ques 15: Calculates no. of tiles required to covera rectangular floor

#Input Section

#Floor Dimensions
a = int(input("What is the length of the floor (in m): "))
b = int(input("What is the breadth of the floor (in m): "))
area_floor = a*b

#Tile Dimensions
c = int(input("What is the length of a tile (in m): "))
d = int(input("What is the breadth of a tile (in m): "))
area_tile = c*d

#Logic Section

no_tiles = area_floor//area_tile 

#Ouput Section

print("No. of tiles required to cover a rectangular floor having an area of", area_floor, "sq. meters are",no_tiles + 1,".")
