"""
Print the square of numbers between a given range. Ask the user for a lower number and a higher number,
then print all of the squares of the numbers in that range (inclusive).
Error-check the second number to make sure it is higher than the first.
"""

# get to the inputz
lower_number = int(input("Please enter a number: "))
higher_number = int(input("Please enter a number higher than the first: "))


# ain't no one got time for errors
while higher_number < lower_number:
    print("Error!")
    higher_number = int(input("Please enter a number higher than the first: "))

# print the squares, including the higher number, yes!
for i in range(lower_number, higher_number + 1):
    print("The square of {} is {}".format(i, i**2))