def count_char_occurrences(s, char_to_count):
    
    if not s:
        return 0
    if s[0] == char_to_count:
        return 1 + count_char_occurrences(s[1:], char_to_count)
    else:
        return count_char_occurrences(s[1:], char_to_count)

input_string = "recursive functions are really cool"
char_to_count = "r"
count = count_char_occurrences(input_string, char_to_count)
print(f'The character "{char_to_count}" occurs {count} times in the string.')