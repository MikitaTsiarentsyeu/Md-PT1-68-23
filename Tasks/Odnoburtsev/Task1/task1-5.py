import random

left_border = input("Please enter the first border of the range: ")
right_border = input("Please enter the second border of the range: ")
borders = (left_border, right_border)

def random_value(x):
    """Returns a random value from the specified range"""
    try:
        a = random.uniform(float(x[0]), float(x[1]))
        print(a)
    
    except ValueError:
        print("The borders should have 'int' or 'float' type")

random_value(borders)
