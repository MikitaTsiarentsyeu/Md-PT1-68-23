import decimal
amount_USD = decimal.Decimal(input('Please enter the amount: '))
ratio = decimal.Decimal(input('Please enter the ratio: '))
amount_BYN = amount_USD * ratio
print("the answer is", amount_BYN)