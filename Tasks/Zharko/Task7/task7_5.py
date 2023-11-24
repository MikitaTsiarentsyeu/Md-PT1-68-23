dict = {}

def decorator(func):
    def wrapper(*args):
        if args in dict:
            return print(f"Cash value: {dict[args]}")
        else:
            dict[*args] = func(*args)
            return print(f"New value: {dict[args]}")
    return wrapper

@decorator
def some_func(a, b):
    return a * b

some_func(2, 3)
some_func(4, 3)
some_func(3, 3)
some_func(2, 3)
print(dict)