"""
Write a function that calculates which of two products is cheaper based on a quantity and price.
The function will take 4 parameters - the quantity and price of each product,
and output either "First" or "Second".
"""

def main():
    print("For the first product, enter the following:")
    first_quantity = int(input("Quantity: "))
    first_price = float(input("Price: $"))
    print("For the second product, enter the following:")
    second_quantity = int(input("Quantity: "))
    second_price = float(input("Price: $"))
    calculate_which_product_cheaper(first_quantity, first_price, second_quantity, second_price)

def calculate_which_product_cheaper(first_quantity, first_price, second_quantity, second_price):
    first_total_cost = first_quantity * first_price
    second_total_cost = second_quantity * second_price

    if first_total_cost < second_total_cost:
        print("First")
    else:
        print("Second")

main()