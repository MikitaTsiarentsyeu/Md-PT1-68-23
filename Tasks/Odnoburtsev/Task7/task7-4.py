import time

def log_file(func):
    def wrapper(n):       
        start_time = time.time()
        res = func(n)
        finish_time = time.time()
        total_exec_time = finish_time - start_time
        with open("log.txt", "w") as f:
            a = f.write(f"The total code execution time is equal to {total_exec_time}\n\
The argument is {n}\nThe output of the function is {res}")        
        return a
    return wrapper

@log_file

def test_func(n):
    l = [i**i for i in range(n)]
    return l

test_func(1000)
