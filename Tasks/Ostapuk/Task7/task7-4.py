import time
def decorator(func):
    def inner(*args, **kwargs):
        start = time.time()
        result_func = func(*args, **kwargs)
        end = time.time()
        res_time = end - start
        with open("example.txt", 'w') as f:
            return f.write(f'''the execution time is {res_time}; arguments are {*args,}; value of a function is {result_func}.''')
    return inner
@decorator
def sum_numbers(a=1, b=3, c=5):
    sum = a+b+c
    return sum
sum_numbers(10, 15, 20)