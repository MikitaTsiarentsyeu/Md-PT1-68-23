def reverse_strings(list_of_strings):
    reversed_strings = []
    for string in list_of_strings:
        reversed_string = string[::-1]
        reversed_strings.append(reversed_string)
    return reversed_strings
strings = ["dog", "clown", "green"]
result = reverse_strings(strings)
print(result)