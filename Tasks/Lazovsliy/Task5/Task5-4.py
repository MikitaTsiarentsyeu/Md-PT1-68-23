def count_lower_and_upper_case_letters(input_string):
    lower_count = sum(1 for char in input_string if char.islower())
    upper_count = sum(1 for char in input_string if char.isupper())
    return lower_count, upper_count

# Example usage:
input_str = "I love python"
lower_count, upper_count = count_lower_and_upper_case_letters(input_str)
print("Lowercase count:", lower_count)
print("Uppercase count:", upper_count)