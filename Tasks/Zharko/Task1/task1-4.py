import decimal

byn = int(input("Enter please amount(BYN): "))
kurs = decimal.Decimal('3.2')
usd = byn / kurs
print("Amount(USD) =", usd)