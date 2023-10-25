def power(x, y):
    '''This recursive function calculates the power of a given number'''
    if y == 0:
        return 1
    if y == 1:
        return x
    return power(x, y-1) * x
x = int(input('Enter the number: '))
y = int(input('Enter the power: '))
print(power(x,y))