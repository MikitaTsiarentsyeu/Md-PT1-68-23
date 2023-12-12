from functools import wraps

def cache(func):
    cache_dict = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Tuples can be dictionary keys because they are immutable, so we convert args and kwargs to a tuple
        cache_key = args + tuple(kwargs.items())
        
        # If the result is already cached, return it
        if cache_key in cache_dict:
            return cache_dict[cache_key]
        
        # Call the function and cache the result
        result = func(*args, **kwargs)
        cache_dict[cache_key] = result
        return result
    
    return wrapper

# Example usage:
@cache
def test_function(x, y):
    print(f"Computing {x} + {y}...")  # This will print when the function actually computes
    return x + y

# Testing with same arguments, should compute only once
print(test_function(2,3))  # Should compute and print "Computing 2 + 3..."
print(test_function(2,3))  # Should not compute again, therefore should not print