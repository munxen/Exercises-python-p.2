#The volume of the cylinder can be calculated by multiplying
# the area of the circle,underlying it, to a height of. Write 
# a program in which the user will set the radius of the cylinder and 
# its height, and in response receiveits volume rounded to one decimal place.

r = int(input("Enter the radius(cm): "))
h = int(input("Enter the height(cm): "))
v = ((r**2)*3.14 * h)
print ("Cylinder area: " + format(v, '.2f')  + " cm" )
