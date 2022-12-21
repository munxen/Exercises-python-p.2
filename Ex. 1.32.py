#Develop a program that asks the user for a four-digit integer and 
# calculates the sum of its constituent digits. For example, if the 
# user enters the number 3141, the program should outputthe following result: 3 + 1 + 4 + 1 = 9.

x = (input("Enter the num: "))
y = 0
for z in x:
    y += int(z)
print ("Nums sum is: " + str(y))