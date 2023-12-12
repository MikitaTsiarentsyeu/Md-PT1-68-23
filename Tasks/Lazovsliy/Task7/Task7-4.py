import time
from functools import wraps

def log_execution_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
        finally:
            end_time = time.time()
            execution_time = end_time - start_time
            # Log the details. You could write these to a file by opening a file in append mode.
            log_message = (
                f"Executing {func.__name__}\n"
                f"Arguments: {args}, {kwargs}\n"
                f"Return Value: {result}\n"
                f"Execution time: {execution_time:.4f} seconds\n"
            )
            print(log_message)  # Replace with file write if necessary
        return result
    return wrapper

# Example usage:
@log_execution_info
def test_function(x, y):
    return x + y

# Test the function to see the output
test_function(4, 5)