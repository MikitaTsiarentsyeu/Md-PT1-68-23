str = 'Hi! How are you?'


def sum_chars(s):
    'a function that takes a string as an argument and returns two numbers, first for count of lower case letters, second for count of the upper case letters in the initial string'
    count_upper_char = 0
    count_lower_char = 0
    for i in range(len(s)):
        if s[i].isupper():
            count_upper_char += 1
        elif s[i].islower():
            count_lower_char += 1
        else:
            continue
    return count_lower_char, count_upper_char


print(f"lower and upper chars:{sum_chars(str)} ")
