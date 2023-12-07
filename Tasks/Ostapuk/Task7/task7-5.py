import functools

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
        else:
            result = cache[key]
        return result
    return wrapper
@memoize
def add_numbers(a, b):
    print("Computing sum...")
    return a + b
result1 = add_numbers(3, 5) 
result2 = add_numbers(3, 5)  
print(result2)