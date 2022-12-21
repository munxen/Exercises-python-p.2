#Many people on the planet are used to calculating a person's height in feet
#and inches, even if the metric system is adopted in their country. Write
#a program that will ask the user for the number of feet,
#and then inches in his height. After that, she should recalculate the height
#in centimeters and display it on the screen

feet = int(input("Enter your height (in feet):"))
inch = int(input("Enter your height (in inch):"))
centimetre = (feet*12 + inch)*2.54 #converting to the metric system
print ("Your height: " + str(centimetre) + " cm.")