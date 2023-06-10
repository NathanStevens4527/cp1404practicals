"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_THRESHOLD = 1000
LOW_BONUS = 0.1
HIGH_BONUS = 0.15
sales = float(input("Enter sales: $"))
while sales > -1:
    if sales < BONUS_THRESHOLD:
        bonus = sales * LOW_BONUS
    elif sales >= BONUS_THRESHOLD:
        bonus = sales * HIGH_BONUS
    print("{:.2f}".format(bonus))
    sales = float(input("Enter sales: $"))