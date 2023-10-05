def reverse_string(input_string):
    # Use string slicing to reverse the input string
    reversed_string = input_string[::-1]
    
    return reversed_string

# Prompt the user for input
user_input = input("Enter a string: ")

# Reverse the input string
result = reverse_string(user_input)

# Display the reversed string
print("Reversed string:", result)