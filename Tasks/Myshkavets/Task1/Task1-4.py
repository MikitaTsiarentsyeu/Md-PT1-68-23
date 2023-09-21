# Function to convert USD to BYN

exchange_rate = 3.25

usd_amount = int(input("Enter amount in USD: "))
byn_amount = usd_amount * exchange_rate
print(f"{usd_amount} USD is {byn_amount} BYN")
