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


payouts_per_year = None
time = None
amount = None

