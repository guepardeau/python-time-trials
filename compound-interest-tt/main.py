while True:
    currency = input("Select Currency ($ for USD, £ for GBP, € for EUR)")
    if currency == "$" or currency == "£" or currency == "€":
        break
    else:
        print("Please input either $, £ or €: ")


principal = None
interest_rate = None
payouts_per_year = None
time = None
amount = None

