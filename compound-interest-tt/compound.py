def compound (amount, principal, interest_rate, payouts_per_year, time):
    amount = principal * (1+interest_rate/payouts_per_year)**(payouts_per_year * time)
    return amount