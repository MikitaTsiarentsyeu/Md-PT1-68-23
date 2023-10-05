# 6. Write a program that takes a string as input
# and returns the string with all vowels removed.

vowels = set('aeiouyаиоуыэеёюя')


def no_vowels(string: str):
    no_vow = ''
    for i in string:
        if i.lower() not in vowels:
            no_vow += i
    return no_vow


print(no_vowels(input('Enter your string:\n')))