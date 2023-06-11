"""
program for shop to calculate total cost of items
asks the user for the number of items and then a price for each
the total is calculated by adding the most recent item price on each cycle of the loop
if the total exceeds 100 a 10% discount is applied.
"""
DISCOUNT_THRESHOLD = 100
total_cost = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range (0, number_of_items):
    item_cost = float(input("Item cost: "))
    total_cost += item_cost
if total_cost > DISCOUNT_THRESHOLD:
    total_cost = total_cost * 0.9
    print(f"Total price for {number_of_items} items is ${total_cost} with a 10% discount")
else:
    print(f"Total price for {number_of_items} items is ${total_cost}")