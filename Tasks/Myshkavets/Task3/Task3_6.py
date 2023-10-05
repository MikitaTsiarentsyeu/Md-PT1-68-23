#Write a program that takes a string as input and returns the string with all vowels removed.

input_string = input("Enter a string: ")
result = ''.join([char for char in input_string if char.lower() not in 'aeiou'])
print(result)