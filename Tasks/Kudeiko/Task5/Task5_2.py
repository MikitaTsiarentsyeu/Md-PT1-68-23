# 2. Write a function that takes a list of strings as an argument and
# returns a new list of strings that are all reversed.
def revers_str(string):
    return string[::-1]


def list_str(lst):
    lst_revers = []
    for i in lst:
        if isinstance(i, str):
            lst_revers.append(revers_str(i))
    return lst_revers


lst = list_str([
    '2.', 'Write', 'a', 'function', 'that', 'takes', 'a',
    'list', 'of', 'strings', 'as', 'an', 'argument', 'and',
    'returns', 'a', 'new', 'list', 'of', 'strings', 'that',
    'are', 'all', 'reversed.'
])
print(lst)
