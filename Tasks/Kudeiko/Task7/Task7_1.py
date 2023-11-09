# 1. Write a function that takes two numbers as input and returns their division.
# Handle the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero.

def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(div(int(input("Enter integer: ")), int(input("Enter integer: "))))