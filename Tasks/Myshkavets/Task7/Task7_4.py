import functools
import time

def log_to_file(log_file):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            with open(log_file, 'a') as file:
                file.write(f"Function: {func.__name__}\n")
                file.write(f"Arguments: {args}, {kwargs}\n")
                file.write(f"Return Value: {result}\n")
                file.write(f"Execution Time: {end_time - start_time:.2f} seconds\n\n")

            return result

        return wrapper

    return decorator

# Usage example:
log_file_path = r'C:\Users\Lenovo\Downloads\Python\Pyth\Task7_4.txt'

@log_to_file(log_file_path)
def example_function(a, b):
    return a + b

result = example_function(2, 3)
