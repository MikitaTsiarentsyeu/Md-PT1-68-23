def remove_vowels(input_string):
    # Define a set of vowels in both uppercase and lowercase
    vowels = set('aeiouAEIOU')
    
    # Initialize an empty string to store the result
    result_string = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        if char not in vowels:
            result_string += char
    
    return result_string

# Prompt the user for input
user_input = input("Введите строку: ")

# Remove vowels from the input string
result = remove_vowels(user_input)

# Display the result
print("Строка без гласных букв:", result)