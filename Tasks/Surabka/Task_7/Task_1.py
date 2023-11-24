m, n = int(input(f'Enter the first number: ')), int(input(f'Enter the second number: '))
'''This function takes two numbers as input and returns their division'''
def division(m, n):
    try:
        return f'The result is {m/n}'
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(division(m, n))