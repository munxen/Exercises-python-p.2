#Write a program in which the user will enter the coordinates of 
# two points on Earth (latitude and longitude) in degrees.
#At the output, weshould get the distance between these points
# when following theshortest path on the surface of the planet.

import math

t_1 = float(input("Enter the latitude of the first point: "))
g_1 = float(input("Enter the longitude of the first point: "))
t_2 = float(input("Enter the latitude of the second point: "))
g_2 = float(input("Enter the longitude of the secon point: "))
distance = 6371.01*math.acos(math.sin(math.radians(t_1)) * math.sin(math.radians(t_2))
            + math.cos(math.radians(t_1)) * math.cos(math.radians(t_2))
            * math.cos((math.radians(g_1)) - (math.radians(g_2))))
print ("Distance: " + format(distance,'.2f') + "-km")