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

interest_rate = None
payouts_per_year = None
time = None
amount = None

