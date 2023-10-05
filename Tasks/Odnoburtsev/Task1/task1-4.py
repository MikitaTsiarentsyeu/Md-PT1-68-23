import decimal
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://kurs.onliner.by/")
soup = BeautifulSoup(html, features="html.parser")
USD_BYN = f"{soup.find_all('p', {'class':('value','value fall', 'value rise')})[2].text}"
USD_BYN = USD_BYN.replace(",", ".")[0:6]

amount_USD = decimal.Decimal(input("Please enter the amount of USD to convert: "))

def converter_to_BYN(x):
    """Converts the amount of money form USD to BYN"""

    if x <= 0:
        print("Hey, guy, you should earn money first :)")

    else:    
        y = x * decimal.Decimal(USD_BYN)
        print(f"USD/BYN ratio set by the National Bank is {USD_BYN} BYN/USD")
        print("The amount in BYN is", y)

converter_to_BYN(amount_USD)


