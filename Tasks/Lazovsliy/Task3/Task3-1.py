def count_vowels(input_string):
    # Define a set of vowels in both uppercase and lowercase
    vowels = set('aeiouAEIOU')
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Prompt the user for input
user_input = input("Введите строку: ")

# Count the vowels in the input string
vowel_count = count_vowels(user_input)

# Display the result
print("Количество гласных букв в строке:", vowel_count)