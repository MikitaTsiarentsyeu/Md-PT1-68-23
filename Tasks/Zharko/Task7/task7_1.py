x = int(input("Enter please first number: "))
y = int(input("Enter please second number: "))

def func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
print(func(x, y))