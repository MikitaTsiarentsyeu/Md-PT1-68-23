
def reverse_strings_in_list(string_list):
    
    reversed_list = []
    
    for string in string_list:
        reversed_string = string[::-1]  # Reversing the string
        reversed_list.append(reversed_string)

    return reversed_list

input_list = ["hello", "world", "python"]
reversed_list = reverse_strings_in_list(input_list)
print(reversed_list)