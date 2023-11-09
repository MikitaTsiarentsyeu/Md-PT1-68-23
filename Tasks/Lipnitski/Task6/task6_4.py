x = int(input('Enter the number:'))
n = int(input('Enter the power more than 0:'))


def get_power_number(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return get_power_number(x, n-1) * x


print(get_power_number(x, n))
