#Imagine that you have opened a savings account in a bank at 4% a year.
#The bank calculates the interest at the end of the year and adds it to the account amount. 
#Write a program that asks the user for the amount of the first initial deposit,
# after which it calculates and displays the amounton the account at the end
# of the first, second and third years. All amounts must be rounded to two decimal places.

x = int(input("Enter the sum of start deposit (in dollars $): "))
first_year = x + (x/100*4)
second_year = first_year + (first_year/100*4)
thrird_year = second_year + (second_year/100*4)
print ("The first year: " + format(first_year,'.2f')  + "$")
print ("The second year: " + format(second_year,'.2f') + "$")
print ("The third year: " + format(thrird_year,'.2f') + "$")