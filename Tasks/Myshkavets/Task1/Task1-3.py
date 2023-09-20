# Function to convert kilometers per hour to meters per second

kph = float(input("Enter speed in kilometers per hour: "))
mps = kph * 1000 / 3600
print(f"{kph} km/h is {mps} m/s")