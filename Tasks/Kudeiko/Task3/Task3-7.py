# 7. Write a program that takes a string as input and returns
# the string with all capital letters converted to lowercase and vice versa.

def letters(string: str):
    rev = ''
    for i in string:
        if i.isalpha():
            if i == i.lower():
                rev += i.upper()
            else:
                rev += i.lower()
        else:
            rev += i
    return rev


print(letters(input('Enter your string:\n')))
