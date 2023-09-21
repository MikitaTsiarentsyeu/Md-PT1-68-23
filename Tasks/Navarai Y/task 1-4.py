import decimal
import math


U = decimal.Decimal(input("USD "))
K = decimal.Decimal(input("Ruble's exchange rate "))
B = U*K
print("BYN",B)


