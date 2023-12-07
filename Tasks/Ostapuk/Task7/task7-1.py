n = int(input("Enter please first number: "))
d = int(input("Enter please second number: "))

def divide_numbers(n, d):
    try:
        result = n / d
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
result = divide_numbers(n, d)
print(result)
