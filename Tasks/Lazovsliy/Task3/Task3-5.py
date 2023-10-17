def filter_strings_by_length(strings, min_length=6):
    # Initialize an empty list to store the filtered strings
    filtered_strings = []
    
    # Iterate through the list of strings
    for string in strings:
        if len(string) > min_length:
            filtered_strings.append(string)
    
    return filtered_strings

# Prompt the user for input by taking a comma-separated list of strings
input_str = input("Введите список строк, разделенных запятой: ")

# Split the input string into a list of strings
input_list = input_str.split(',')

# Filter the list to include only strings longer than 5 characters
filtered_list = filter_strings_by_length(input_list, min_length=6)

# Display the filtered list
print("Строки с длиной больше 5 символов:", filtered_list)