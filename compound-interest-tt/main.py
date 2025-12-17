from compound import compound

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
        if interest_rate >= 0:
            interest_rate = interest_rate/100
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

while True:
    try:
        time = int(input("Enter the number of years you plan to invest: "))
        if time > 0:
            break
        else:
            print("The number of years must be positive: ")
    except ValueError:
             print("Please enter the integer of years you're investing e.g '8' for 8 years: ")

amount = 0
amount = compound(amount, principal, interest_rate, payouts_per_year, time)
print((f"Your total after {time} year(s) is {currency}{amount:.2f}."))   

