#Imagine that the amount for using taxi services consists of
# a base fare of $4.00 plus $0.25 for every 140 m of the trip. 
#Write a function that takes as the only parameter the distance 
# of the trip in kilometers and returns the total amount of the 
# taxi payment. The main program should show the result of the function call.

distance = int(input("Enter distance (in meters): "))

def taxi(d):
    """taxi counter"""
    price = (d/1000)*0.25 + 4
    print ("Price for taxi: " + str(price) + "$")

taxi(distance)