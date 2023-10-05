#Write a program that takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.

input_strings = input("Enter a list of strings separated by spaces: ").split()
result = [s for s in input_strings if len(s) > 5]
print(result)