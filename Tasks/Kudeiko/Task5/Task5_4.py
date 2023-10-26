#4. Write a function that takes a string as an argument and returns
# two numbers, first for count of lower case letters, second for count
# of the upper case letters in the initial string.


def count_word(string: str):
    count_of_lower = 0
    count_of_upper = 0
    for i in string:
        if i.islower():
            count_of_lower += 1
        elif i.isupper():
            count_of_upper += 1
        else:
            continue
    return (f'Count of lower case letters: {count_of_lower}.\n'
            f'Count of upper case letters: {count_of_upper}.')


sentence = count_word("""
Buddy you're a boy make a big noise
Playin' in the street gonna be a big man some day
You got mud on yo' face
You big disgrace
Kickin' your can all over the place
Singin'
""")

print(sentence)