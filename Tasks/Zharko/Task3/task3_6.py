test_string = "Write a program that takes a string as input and returns the \
string with all vowels removed."
VOWELS = "aeiouyауоыэяюёие" # Vowels of the Russian and English alphabet
new_string = ""

for i in test_string:
    if i.lower() not in VOWELS:
        new_string += i
print(new_string)
