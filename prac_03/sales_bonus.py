

sales = float(input("Enter sales: $"))
while sales != 0:
    if sales < 1000:
        bonus = sales * .1
        print("Bonus: ${:.2f}".format(bonus))
    elif sales >= 1000:
        bonus = sales * .15
        print("Bonus: ${:.2f}".format(bonus))
    else:
        print("Invalid amount")
        sales = float(input("Enter sales: $"))
    print("Thank you.")
