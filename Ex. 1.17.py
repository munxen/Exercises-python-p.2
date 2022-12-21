#Write a program that asks the user for the mass of waterand the required 
# temperature difference. At the output, you should get the amount of energy 
# that needs to be added or subtracted to achievethe desired temperature change.
#Expand your program in such a way that the cost of accompanying water heating
# is also displayed. It is usually customary to measureelectricity in kWh, not 
# in joules. For this example, let's assumethat electricity costs us 8.9 cents 
# per kWh. Useyour program to calculate the cost of heating one cup of coffee.

m_h2o = int(input("Enter the water weight (gr): "))
x = int(input("Enter the temperature difference (c*): "))
q = m_h2o * 4.186 * x
price = q/3600000*8.9
print ("The amount of energy required to raise the temperature: " + str(q))
print ("Price for enegry " + format(price, '.2f') + ' cents.' )
print ("Price for 1 cup coffe " + format(price, '.2f') + ' cents.' )