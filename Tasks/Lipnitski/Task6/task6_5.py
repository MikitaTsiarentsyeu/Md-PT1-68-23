n = int(input('Enter the number more than 0:'))


def get_num_fibonacci(n, x=0, y=1):
    if n == 1:
        return y
    else:
        prev = y
        y = x + y
        x = prev
        y = get_num_fibonacci(n-1, x, y)

    return y


print(get_num_fibonacci(n))
