def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base = 10
exponent = 5
result = power(base, exponent)
print(f'{base}^{exponent} = {result}')