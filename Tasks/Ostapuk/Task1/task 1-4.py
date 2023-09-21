import decimal
M = decimal.Decimal(input("Enter the amount of USD "))
D = decimal.Decimal(3.26)
BYN = D * M
print("The amount of money after the transfer from USD to BYN ", BYN)