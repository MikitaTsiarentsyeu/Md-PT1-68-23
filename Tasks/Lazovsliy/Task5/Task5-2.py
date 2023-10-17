def reverse_strings_in_list(string_list):
    reversed_list = [string[::-1] for string in string_list]
    return reversed_list

# Example usage:
input_list = ["python", "C++", "C#"]
reversed_list = reverse_strings_in_list(input_list)
print("Reversed list:", reversed_list)