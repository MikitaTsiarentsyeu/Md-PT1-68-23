#Write a program that takes a string as input from a user and returns the number of vowels in the string

def count_vowels(string):
    
    string = string.lower()
    vowels = "aeiou"
    
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
    
    return count

input_string = input("Enter the line: ")

vowel_count = count_vowels(input_string)
print(f"Number of vowels per line: {vowel_count}")