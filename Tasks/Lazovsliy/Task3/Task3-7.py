
def swap_case(input_string):
    # Initialize an empty string to store the result
    swapped_string = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        if char.islower():
            swapped_string += char.upper()
        elif char.isupper():
            swapped_string += char.lower()
        else:
            swapped_string += char
    
    return swapped_string

# Prompt the user for input
user_input = input("Введите строку: ")

# Swap the case of characters in the input string
result = swap_case(user_input)

# Display the result
print("Строка с обменом регистра букв:", result)