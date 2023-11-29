x = int(input("Enter the numerator: "))
y = int(input("Enter the denominator: "))


def get_division(x, y):
    try:
        d = (x / y)
        return d
    except ZeroDivisionError:
        print("Cannot divide by zero")


print(get_division(x, y))
