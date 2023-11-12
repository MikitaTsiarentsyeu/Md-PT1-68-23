lst_1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst_2 = ["1", 2, 3, (4, 5, 6), 7, 8]
lst_3 = {1, 2, 3, 4, 5, 6, 7, 8}


def get_sum_even_numbers(l):
    sum = 0
    try:
        for i in range(len(l)):
            if l[i] % 2 == 0:
                sum = sum + l[i]
        return sum

    except TypeError:
        if not isinstance(l, list):
            print('Invalid input type')
        else:
            for value in l:
                if not isinstance(value, int):
                    print('Invalid value type')


print(get_sum_even_numbers(lst_1))
print(get_sum_even_numbers(lst_2))
print(get_sum_even_numbers(lst_3))
