def power(a, b):
    '''Recursive function to calculate the power of a given number.'''
    if b == 1:
        return a
    return a * power(a, b - 1)

print(power(2, 7))