def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
base = 2
exponent = 3
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
