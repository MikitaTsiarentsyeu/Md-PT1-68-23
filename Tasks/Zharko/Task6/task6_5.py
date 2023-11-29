def fibonacci(n):
    '''Recursive function to find the Nth number in the Fibonacci sequence'''
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(60))
