def cache(func):
    def wrapper(n):
        # global cache_dict
        if n not in cache_dict:
            cache_dict[n] = func(n)
        return cache_dict[n]
    return wrapper

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

cache_dict = {}
n = int(input())
print(fib(n))
# print(cache_dict)
