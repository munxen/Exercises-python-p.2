#For this exercise, you will need to write a program
#that will ask the user for the distance in feet. 
#Thereafter she will have to convert this number 
# into inches, yards and miles and put it on the screen.
# You can easily find coefficients for unit conversionon the Internet.

feet = int(input("Enter the distance in feet: "))
print ("In inch: " + str(feet*12))
print ("In yard: " + str(feet*0.33))
print ("In milies: " + str(feet*0.00019))