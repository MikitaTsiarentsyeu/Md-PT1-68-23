def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Example usage:
print(divide_numbers(10, 2))  # Should return 5.0
print(divide_numbers(10, 0))  # Should return "Cannot divide by zero"