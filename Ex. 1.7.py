#Write a program that asks the user for a number and 
# calculates the sum of positive natural numbers
# from 1 to the value entered by the user.

x = int(input("Enter the num "))
numbers = list(range(1, x+1))
print("Sum all numbers " + str(sum(numbers)))