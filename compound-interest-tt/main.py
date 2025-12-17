while True:
    currency = input("Select Currency ($ for USD, £ for GBP, € for EUR)")
    if currency == "$" or currency == "£" or currency == "€":
        break
    else:
        print("Please input either $, £ or €:")

while True:
    try:
        principal = (float(input("Please enter Principal (e.g. 10500)")))
        if principal > 0:
            break
        else:
            print("Principal must be greater than 0: ")
    except ValueError:
        print("Please enter a Numerical Value only: ")

while True:
    try:
        interest_rate = (float(input("Please enter the interest rate (e.g. 2.5): ")))
        if interest_rate > 0:
            break
        else:
            print("Interest Rate must be greater than 0: ")
    except ValueError:
        print("Please enter a Numerical Value only: ")

while True:
        payouts_per_year = (input("Please enter how often you are expecting to be paid interest, i.e Daily, Monthly or Yearly: ").strip().lower())
        if payouts_per_year == "daily":
            payouts_per_year = 365
            break
        elif payouts_per_year == "monthly":
            payouts_per_year = 12
            break
        elif payouts_per_year == "yearly":
            payouts_per_year = 1
            break
        else:
            print(f"{payouts_per_year} is not valid. Please type daily, monthly or yearly: ")

time = None
amount = None

