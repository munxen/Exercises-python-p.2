#In this exercise, we will expand the situation from the previous task. 
#This time you have to write a program in which the user it will enter
# a time interval in the form of the total number of seconds,after which 
# the same duration should be shown on the screen in the formatD:HH:MM:SS, 
# where D, HH, MM and SS are the number of days, hours, minutes and seconds, 
# respectively. At the same time, the last three values should be entered 
# in a two-digit format, as we are used to seeing them on an electronic clock. 
# Try to find out for yourself which characters need to be enteredinto the 
# format specifier so that, if necessary, the numbers are supplementedon the 
# left with zeros instead of spaces.

from datetime import datetime

full_time = int(input("Enter the full time in seconds: "))
print(datetime.fromtimestamp(full_time).strftime("%d:%I:%M:%S"))
