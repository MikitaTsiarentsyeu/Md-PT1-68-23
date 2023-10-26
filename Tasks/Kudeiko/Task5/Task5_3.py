# 3. Write a function that takes a list of strings as an argument
# and returns a new list with all the strings that have a
# length greater than 5.


def list_str(lst):
    lst_gr5 = []
    for i in lst:
        if isinstance(i, str) and len(i) > 5:
            lst_gr5.append(i)
    return lst_gr5


fin_lst = list_str([
    '3.', 'Write', 'a', 'function', 'that', 'takes', 'a',
    'list', 'of', 'strings', 'as', 'an', 'argument', 'and',
    'returns', 'a', 'new', 'list', 'with', 'all', 'the',
    'strings', 'that', 'have', 'a', 'length', 'greater', 'than', '5.'
])

print(fin_lst)