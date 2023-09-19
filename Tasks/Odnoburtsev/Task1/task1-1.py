temp_C = input("Please enter the temperature in degrees Celcius: ")

def temp_F (a):
    """Returns temperature in degrees Fahrenheit based on degrees Celcius"""
    try:
        if float(a) < -273.15:
            print("The temperature must be greater than -273.15 degrees Celcius")
        else:
            b = float(a) * 9/5 + 32
            print(f"The temperature is {b} degrees Fahrenheit")

    except ValueError:
        print("The value should have 'int' or 'float' type")

temp_F(temp_C)