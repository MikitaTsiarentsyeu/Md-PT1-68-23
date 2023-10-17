def count_words(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Initialize an empty dictionary to store word counts
    word_count = {}
    
    # Iterate through the words and count their occurrences
    for word in words:
        # Remove punctuation and convert to lowercase for consistent counting
        cleaned_word = word.strip('.,!?').lower()
        
        # Update the word count in the dictionary
        if cleaned_word in word_count:
            word_count[cleaned_word] += 1
        else:
            word_count[cleaned_word] = 1
    
    return word_count

# Prompt the user for input
user_input = input("Введите строку: ")

# Calculate the word counts in the input string
word_counts = count_words(user_input)

# Display the result as a dictionary
print("Словарь с количеством слов:")
for word, count in word_counts.items():
    print(f"{word}: {count}")