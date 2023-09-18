# 1.Write a program that converts Celsius to Fahrenheit,
# ask a user for the Celsius value.


def converter_dg():
    celsius = float(input("Please, enter temperature in Celsius: "))
    while celsius >= -273.15:
        fahrenheit = celsius * 9 / 5 + 32
        print(f"{celsius} °C equals {fahrenheit:.1f} °F")
        celsius = float(input("Please, enter temperature in Celsius: "))
    else:
        print("The temperature can't be lower than -273.15 °C.\nTry again.")
        converter_dg()


converter_dg()
