#In many countries, a certain deposit is put into the cost of glass containers, 
# to encourage beverage buyers to hand over empty bottles. Admit, 
# bottles with a volume of 1 liter or less cost $0.10, and bottles with a larger volume cost $0.25.
#Write a program asking the user for the number of bottles of each 
# size.The screen should display the amount that can be bailed out if you pass
# all available dishes. Format the output so that the sum includes two characters
# after the comma and supplemented on the left with the dollar symbol.

print ("Course bottles: small/0.10$ | big/0.25$")
small_bottle = int(input("How many small bottles: "))
big_bottle = int(input("How many big bottles: "))
small = small_bottle * 0.1
big = big_bottle * 0.25
print ("Your sum all bottles: $" + str(small+big))