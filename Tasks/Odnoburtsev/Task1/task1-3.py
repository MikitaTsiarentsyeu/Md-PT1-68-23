speed_km_h = input("Please enter the speed in km/h: ")

def speed_m_s (a):
    """Returns the speed in m/s based on the speed in km/h"""
    try:
        if float(a) < 0:
            print("The speed must be greater than or equal to zero")
        else:
            b = float(a) * 1000 / 3600
            print(f"The speed is {b} m/s")

    except ValueError:
        print("The value should have 'int' or 'float' type")

speed_m_s(speed_km_h)