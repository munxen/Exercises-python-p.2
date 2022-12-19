#In the USA, automobile fuel consumption is calculated in miles pergallon (miles-per-gallon – MPG).
#At the same time, in Canada , this indicator it is usually expressed
#  in liters per 100 km (liters-per-hundred kilometers – L/100 km).
#Use your research abilities to determine the formula for converting the first units 
# of calculus into the last ones. Afterthat, write a program that asks the userfor 
# the fuel consumption indicator of the car in American units and displays it on 
# the screen in Canadian units.

a = int(input("Enter the MGP of you car: "))
print ("Indicator you car is " + str(235.22/a) + " L" + "/km")
