# 1. Write a program that takes a string as input from a user and
# returns the number of vowels in the string.

vowels = set('aeiouyаиоуыэеёюя')


def count_vowels(string: str):
    count = 0
    for i in string.lower().strip():
        if i.isalpha():
            if i in vowels:
                count += 1
    return f'The number of vowels is equal: {count}'


print(count_vowels(input('Enter your string:\n')))
