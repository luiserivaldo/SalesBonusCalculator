"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    bonus = sales
    if sales < 1000:
        bonus = bonus*0.1
    elif sales >= 1000:
        bonus = bonus*0.15
    print("Bonus: ", bonus)
    sales = float(input("Enter sales: $"))
    if sales < 0:
        print("You have entered a negative number.")
