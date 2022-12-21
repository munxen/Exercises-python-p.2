#Write a program that will ask the user for the radiusand
# save it in the variable r. After that, it should calculate
# the area of a circle with a given radius and the volume of
# a ball with the same radius. Use the constant pi from the
# math module in your calculations.

r = int(input("Enter the radius (cm) "))
sqare_cirle = (r**2) * 3.14
circle_volume = 4/3 * 3.14 * (r**3)
print ("Circle sqare: " + format(sqare_cirle, '.2f') + " cm.")
print ("Cirlce volume: " + format(circle_volume, '.2f') + " cm.")