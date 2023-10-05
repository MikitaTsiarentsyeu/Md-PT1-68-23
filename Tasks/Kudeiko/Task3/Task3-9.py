# 9. Write a program that takes a string as input and
# returns the string reversed.

# reversed_string = input()[::-1]
# print(reversed_string)


def revers_str(string: str):
    rev_str = ''
    for i in string[::-1]:
        rev_str += i
    return rev_str


print(revers_str(input('Enter your string:\n')))


