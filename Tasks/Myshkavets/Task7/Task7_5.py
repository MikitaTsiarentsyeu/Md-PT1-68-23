import functools

def cache_decorator(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

@cache_decorator
def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

result1 = add(2, 3)
result2 = add(2, 3) 
result3 = add(4, 5)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")