def summa (a: int, b: int):
    '''This function will summarize only int values'''
    return a+b

a, b = int(input(f'Enter the first number: ')), int(input(f'Enter the second number: '))
print(f'Summa is {summa(a, b)}')
