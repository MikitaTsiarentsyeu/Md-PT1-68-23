# 5. Write a program that takes a list of strings as input and returns
# a list with all strings that have a length greater than 5 characters.
import sys

print('Enter your strings separated by spaces:')
s = sys.stdin.readlines()
lst_in = list(map(str, (i.replace('\n', '') for i in s)))


def len_string(lst):
    return [i for i in lst if len(i) > 5]


print(len_string(lst_in))
