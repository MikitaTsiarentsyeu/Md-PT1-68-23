import decimal

K = decimal.Decimal(input("exchange rate $ "))
U = decimal.Decimal(input("quantity $ "))

B = U*K
print(B,"BYN")