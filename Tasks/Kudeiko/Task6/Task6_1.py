# 1. Write a recursive function to reverse a string.

def revers_string_rec(string: str, rev_str=''):
    if not len(string):
        return rev_str
    rev_str += string[-1]
    return revers_string_rec(string[:-1], rev_str)


print(revers_string_rec("1. Write a recursive function to reverse a string."))