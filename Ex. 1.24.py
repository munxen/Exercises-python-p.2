#Create a program in which the user can enter a timeinterval in 
# the form of the number of days, hours, minutes and seconds and 
# find out the totalnumber of seconds that make up the entered segment.

d = int(input("Enter the days: "))
h = int(input("Enter the hours: "))
m = int(input("Enter the minuts: "))
s = int(input("Enter the seconds: "))
full_time = d*216000 + h*3600 + m*60 + s
print ("Full time is " + str(full_time) + " seconds.")