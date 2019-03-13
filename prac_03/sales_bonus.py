"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    sales = float(input("Enter sales: $"))
    print(compute_bonus(sales))
    print("Thank you.")


def compute_bonus(sales):
    while sales != 0:
        if sales < 1000:
            bonus = sales * .1
            return "Bonus: ${:.2f}".format(bonus)
        elif sales >= 1000:
            bonus = sales * .15
            return "Bonus: ${:.2f}".format(bonus)
        else:
            return "Invalid amount"


main()
