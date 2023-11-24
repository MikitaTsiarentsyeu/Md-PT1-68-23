import random

dict = {}
for i in range(6):
    dict[i] = i**2
print(f"The current dictionary is {dict}")

def cash_dict(func):
    def wrapper(n):
        # if n in dict:
        try:
            return (f"An argument '{n}' is present in the dictionary. A cached value is '{dict[n]}'.\n\
The existing dicionary remains unchanged and equals to {dict}")
        # else:
        except:
            dict[n] = func(n)
            return (f"An argument '{n}' is absent in the dictionary. A computed value is '{func(n)}'.\n\
A new dictionary is {dict}")
    return wrapper

@cash_dict

def square(n):
    res = n**2
    return res

random_number = random.sample(range(10), 3)
for k in random_number:
    print(square(k))
        