# 4.Write a program that converts some amount of money from USD to BYN,
# ask a user for the amount, store the ratio inside the program itself.

import decimal as dc


def converter_money():
    rate_15_09_23 = 3.2533
    usd = int(input("How much USD do you want to convert to BYN: "))
    if usd >= 0:
        byn = dc.Decimal(usd * rate_15_09_23)
        print(f'{usd} USD on 15.09.23 is {byn:.2f} BYN')
    else:
        print("Incorrect value.\nTry again.")
    converter_money()


converter_money()
