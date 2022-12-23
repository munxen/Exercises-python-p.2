#Describe a function that accepts the lengths of two legs of a 
# right-angled triangle as input and returns the length of the 
# hypotenuse calculated according to the Pythagorean theorem. 
#In the main program should be carried out requesting the lengths 
# of the sides from the user, calling the function and displaying
# the result on the screen.

a = int(input("First cathet: "))
b = int(input("Second cathet: "))

def hypotenuse(x,y):
    c = (x**2) + (y**2)
    print (c**(0.5))

hypotenuse(a,b)