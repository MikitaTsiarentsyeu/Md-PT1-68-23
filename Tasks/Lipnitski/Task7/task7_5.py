dict = {}


def cash_dict(func):
    def inner(*args):
        if args in dict:
            return f'our cash {dict[args]}'
        else:
            dict[*args] = func(*args)
            return f'new value {dict[args]}'

    return inner


@cash_dict
def sum_numbers(a, b, c):
    return a+b+c


print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2, 3))
print(sum_numbers(4, 3, 4))
