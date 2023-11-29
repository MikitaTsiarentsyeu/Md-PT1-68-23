def count_char_occurrences_recursive(input_string, target_char):
    # Base case: If the string is empty, there are no occurrences.
    if not input_string:
        return 0

    # If the first character of the string matches the target character,
    # increment the count and recursively check the rest of the string.
    if input_string[0] == target_char:
        return 1 + count_char_occurrences_recursive(input_string[1:], target_char)
    else:
        # If the first character doesn't match, check the rest of the string.
        return count_char_occurrences_recursive(input_string[1:], target_char)

# Example usage:
input_str = "hello Mikita, my name Hleb!"
target_char = "e"

count = count_char_occurrences_recursive(input_str, target_char)
print(f"The character '{target_char}' occurs {count} times in the string.")