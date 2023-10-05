#Write a program that takes a string as input and returns a dictionary with the count of each word in the string.

def word_count(string): return {word: string.split().count(word) for word in set(string.split())}

input_string = input("Enter a string: ")
result = word_count(input_string)
print(result)