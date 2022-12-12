#Create a program that asks the user for the length and width
# of the garden plot in feet. Display the area of the plot in acres.

a = float(input("Enter lenght you garden in meters: "))
b = float(input("Enter weight you garden in meters: "))
c = (a*b)/4046.86
print("You garden plot sqare are " + str(c).strip("()") + " acres.")