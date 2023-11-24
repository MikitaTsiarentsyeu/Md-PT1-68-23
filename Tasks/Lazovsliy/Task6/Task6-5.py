def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = 6
result = fibonacci_recursive(n)
print(f"The {n}-th number in the Fibonacci sequence is {result}")