#The programm that you will write should begin with a request from 
# the customer for the amount of the order in the restaurant. After 
# that, the tax and tip to the waiter should be calculated. You can 
# usethe tax rate accepted in your region to calculate the amount of 
# fees. As atip, we will leave 18% of the order value without tax. At 
# the exit, the program should display separately the tax, the tip 
# amount and the total,including both components. Format the output 
# so thatall numbers are displayed with two decimal places.

a = float(input("Enter sum you order: "))
b = a/100*18 #tips
c = a /100*12 #tax
d = b+c #sum
print ("Tips: $" + ("%.2f" % b) + "\nTax: $" 
      + ("%.2f" % c) + "\nAll sum: $" + ("%.2f" % d))
