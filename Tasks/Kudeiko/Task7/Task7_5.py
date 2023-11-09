# 5. Write a decorator function that caches the return value of a function with a dictionary.
# If the function is called again with the same arguments,
# return the cached value instead of computing it again.
import random

dict = {i: chr(i) for i in range(0, 50, 5)}


def decorator(func):
    def wrapper(n):
        if n in dict:
            return f"The number {n} is already in the dictionary and its value is {dict[n]}"
        else:
            dict[n] = func(n)
            return (f"The number {n} has been added to the dictionary, its value is {dict[n]}.\n"
                    f"The updated dictionary now looks like this:\n{dict}")

    return wrapper


@decorator
def chr_num(n):
    return chr(n)


for i in random.sample(range(0, 50), 10):
    print(chr_num(i))
