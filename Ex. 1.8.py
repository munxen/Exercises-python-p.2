#The online store sells various souvenirs and trinkets. 
#Each souvenir weighs 75 g, and the trinket weighs 112 g. 
#Write a pro gram asking the user for the number of those
#and other purchases,then display the total weight of the
#parcel on the screen.

z_x = int(input("Enter the number of souvenirs: "))
z_y = int(input("Enter the number of trinkets: "))
x = 75
y = 112
print ("Total package weight: " + str((x*z_x + y*z_y)/1000) + " kg.")