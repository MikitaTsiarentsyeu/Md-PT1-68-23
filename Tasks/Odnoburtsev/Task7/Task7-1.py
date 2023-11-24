while True:
    try:
        x = float(input("Please enter the x value:\n").replace(",", "."))
        break
    except ValueError:
        print("Only numbers are allowed. Please try again")
        continue

while True:
    try:
        y = float(input("Please enter the y value:\n").replace(",", "."))
        if y == 0:
            raise AttributeError("Zero value for y is not allowed. Please try again")
        break
    except ValueError:
        print("Only numbers are allowed. Please try again")
        continue
    except AttributeError as e:
        print(e)
        continue

def division_func(a, b):
    """Returns a result of a division of two numbers"""

    try:
        res = a/b
        print(f"The answer is {res}")
    except:
        print("ooops, something went wrong")

division_func(x, y)