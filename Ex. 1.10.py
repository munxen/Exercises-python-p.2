# Create a program that asks the user for two integers a and b, and then 
#displays theresults of the following mathematical operations:
#sum of a and b;
#the difference between a and b;
#product of a and b;
#quotient of dividing a by b;
#the remainder of dividing a by b;
#decimal logarithm of the number a;
#the result of raising the number a to the power of b.

import math
a = int(input("Enter the first num: "))
b = int(input("Enter the second num: "))
print ("Sum(+): " + str(a+b))
print ("Difference(-): " + str(a-b))
print ("Multiplier(*): " + str(a*b))
print ("The quotient of the division(/): " + str(a/b))
print ("The remainder of the division(//): " + str(a//b))
print ("Decimal logarithm of first number: " + str(math.log10(a)))
print ("Exponentiation of a and b: " + str(a**b))