#Write a program to calculate the velocity of an object 
# during its contact with the ground. The user must set 
# the height in meters from which the object will be released.

import math
h = int(input("Enter the height (cm): "))
s = (9.8**2) + 2*0*h
s = round(s)
x = math.isqrt(s)
print ("Object speed: " + str(x) + " m/s.")