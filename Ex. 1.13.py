#Imagine that you are writing software for an automated checkout in a self-service store. 
#One of the functions assigned to the cashier should be the calculation of change in case 
# of payment by the buyer in cash. Write a program that will ask the user for the sum
# of change in cents. After that, it should calculate and display on the screen how many
# and what coins will be required to issue the specified amount, provided that the minimum
# possible number of coins should be involved. Let's say we have at our disposal coins of
# 1, 5, 10, 25 cents, as well as 1 (loonie) and 2 (toonie) Canadian dollars.

"""coin values"""
monet_1 = 200
monet_2 = 100
monet_3 = 25
monet_4 = 10
monet_5 = 5
monet_6 = 1
"""formules"""
cash = int(input("Enter the sum in ¢: "))
print (str(cash//monet_1) + " from 2$")
cash = cash % monet_1
print (str(cash//monet_2) + " from 1$")
cash = cash % monet_2
print (str(cash//monet_3) + " from 25¢")
cash = cash % monet_3
print (str(cash//monet_4) + " from 10¢")
cash = cash % monet_4
print (str(cash//monet_5) + " from 5¢")
cash = cash % monet_5
print (str(cash//monet_6) + " from 1¢")
cash = cash % monet_6