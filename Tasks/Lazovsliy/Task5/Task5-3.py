def filter_strings_by_length(string_list):
    filtered_list = [string for string in string_list if len(string) > 5]
    return filtered_list

# Example usage:
input_list = ["chocolate", "USA", "London", "UZDA", "kiwi"]
filtered_list = filter_strings_by_length(input_list)
print("Filtered list:", filtered_list)