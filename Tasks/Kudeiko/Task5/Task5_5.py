# 5. Write a function that takes an ordered list of numbers without
# duplicates and returns a string with ranges for those numbers, check
# the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


def get_ranges(lst):
    lst_new = []
    first = lst[0]
    last = lst[0]
    indx = 0
    while indx != len(lst) + 1:
        if indx == len(lst):
            lst_new.append((first, last))
            indx += 1
            continue
        if lst[indx] - last > 1:
            lst_new.append((first, last))
            first = lst[indx]
            last = lst[indx]
            indx += 1
        else:
            last = lst[indx]
            indx += 1
    return to_str(lst_new)


def to_str(lst_new):
    l = []
    for first, last in lst_new:
        if first != last:
            l.append(f'{first}-{last}')
        else:
            l.append(f'{first}')
    return ', '.join(l)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
