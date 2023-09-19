import math

r = input("Please enter the radius value, in cm: ")

def S_circle (a):
    """Returns the square of the circle based on the radius value"""
    try:
        if float(a) <= 0:
            print("The radius value must be greater than zero")
        else:
            b = math.pi * float(a)**2
            print(f"The square of the circle is {b} cm")

    except ValueError:
        print("The value should have 'int' or 'float' type")

S_circle(r)