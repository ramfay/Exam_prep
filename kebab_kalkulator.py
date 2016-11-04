"""
A calculator that determines the cost of a kebab, based on user input
"""

# constants
SMALL = 7.50
LARGE = 10

# order form
final_price = 0
input_size = str(input("What size? (S)mall or (L)arge?")).lower()
input_toppings = int(input("How many toppings?"))

# charge extra fiddy cents for the third topping and over - the first two still remain free
if input_toppings >= 3:
    for i in range(input_toppings - 2):
        final_price += .50

# now that the toppings are sorted, finally felt like dealing with the actual size here
if input_size == "s":
    final_price += SMALL
else:
    final_price += LARGE

# this is how much richer we shall be
print("Your order price is ${:.2f}.".format(final_price))