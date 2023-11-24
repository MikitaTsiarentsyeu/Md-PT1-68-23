def is_palindrome_recursive(input_string):
    # Base case: If the string has 0 or 1 characters, it's a palindrome.
    if len(input_string) <= 1:
        return True

    # Check if the first and last characters are the same.
    if input_string[0] == input_string[-1]:
        # Recursively check the substring without the first and last characters.
        return is_palindrome_recursive(input_string[1:-1])
    else:
        return False

# Example usage:
input_str1 = "racecar"
input_str2 = "mersedes benz"
input_str3 = "BMW"

print("Is 'racecar' a palindrome?", is_palindrome_recursive(input_str1))  # Output: True
print("Is 'mersedes benz' a palindrome?", is_palindrome_recursive(input_str2))     # Output: False
print("Is 'BMW' a palindrome?", is_palindrome_recursive(input_str3))     # Output: True