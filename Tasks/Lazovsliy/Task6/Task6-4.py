def calculate_power_recursive(base, exponent):
    # Base case: If the exponent is 0, the result is 1.
    if exponent == 0:
        return 1

    # Recursive case: Calculate the power using recursion.
    return base * calculate_power_recursive(base, exponent - 1)

# Example usage:
base = 4
exponent = 2

result = calculate_power_recursive(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")