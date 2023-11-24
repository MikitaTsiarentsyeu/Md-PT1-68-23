def reverse_string_recursive(input_string):
    # Base case: If the string is empty or has only one character, return it as is.
    if len(input_string) <= 1:
        return input_string

    # Recursive case: Reverse the substring excluding the first character,
    # and then append the first character to the end.
    return reverse_string_recursive(input_string[1:]) + input_string[0]

# Example usageCertainly:
input_str = "Hello, Mikita!"
reversed_str = reverse_string_recursive(input_str)
print("Reversed string:", reversed_str)