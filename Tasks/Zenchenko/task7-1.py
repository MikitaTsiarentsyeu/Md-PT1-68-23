a = int(input("Enter the numerator"))
b = int(input("Enter the denominator"))


def devi(n, d):
    try:
        s = (n / d)
        return s
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(devi(a, b))
