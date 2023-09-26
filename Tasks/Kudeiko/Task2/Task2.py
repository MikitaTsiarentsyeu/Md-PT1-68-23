num_time = {1: 'один', 2: 'два', 3: 'три',
            4: 'четыре', 5: 'пять', 6: 'шесть',
            7: 'семь', 8: 'восемь', 9: 'девять',
            10: 'десять', 11: 'одиннадцать', 12: 'двенадцать',
            13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
            16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
            19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
            40: 'сорок', 50: 'пятьдесят'}


def hour_sklan(h: int):
    if h == 1:
        return 'первого'
    elif h == 2:
        return 'второго'
    elif h == 3:
        return f'{num_time[3][:2]}етьего'
    elif h == 4:
        return f'{num_time[4][:3]}вёртого'
    elif h == 7:
        return f'{num_time[7][:2]}дьмого'
    elif h == 8:
        return f'{num_time[8][:3]}ьмого'
    else:
        return f'{num_time[h][:-1]}ого'


def test_input_times(times: str):
    if times[2] != ':' or len(times) != 5:
        exit('Error. Incorrect input. Required format hh:mm.')
    if not times[:2].isdigit() or not times[3:].isdigit():
        exit('Error. You must enter integers in hh and mm format.')

    h, m = map(int, times.split(':'))

    if 0 > h or h > 24:
        exit('Error. The hour cannot be more than 24 or less than 0.')
    if 0 > m or m > 60:
        exit('Error. Minutes cannot be more than 60 or less than 0.')
    if h > 12:
        h = h - 12
    elif h == 0:
        h += 12
    if m == 60:
        m = 0
    return convertor_time(h, m)


def convertor_time(h: int, m: int):
    if m == 0:
        return min_equals0(h)
    if m < 30 and m != 0:
        return min_less30(h, m)
    if m == 30:
        return min_equals30(h)
    if 30 < m < 45:
        return min_less45_and_more30(h, m)
    return minute_more_or_equals45(h, m)


def min_equals0(h: int):
    if h == 1:
        return f'{num_time[h]} час ровно'
    elif 1 < h < 5:
        return f'{num_time[h]} часа ровно'
    else:
        return f'{num_time[h]} часов ровно'


def min_less30(h: int, m: int):
    if m % 10 == 1:
        if m == 1:
            return f'{num_time[m][:2]}на минута {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'
        else:
            return f'{num_time[m - m % 10]} {num_time[m % 10][:2]}на минута {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'
    elif m % 10 in (2, 3, 4):
        if m % 10 == 2:
            return f'{num_time[m][:2]}e минуты {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}' if m == 2 else \
                f'{num_time[m - m % 10]} {num_time[2][:2]}e минуты {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'
        else:
            return f'{num_time[m - m % 10]} {num_time[m % 10]} минуты {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'
    else:
        if 4 < m < 21 or m in (30, 40, 50):
            return f'{num_time[m]} минут {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'
        else:
            return f'{num_time[m - m % 10]} {num_time[m % 10]} минут {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'


def min_equals30(h: int):
    return f'половина {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'


def min_less45_and_more30(h: int, m: int):
    if m % 10 == 1:
        return f'{num_time[m - m % 10]} {num_time[1][:2]}на минута {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'
    elif m % 10 in (2, 3, 4):
        if m % 10 == 2:
            return f'{num_time[m - m % 10]} {num_time[2][:2]}e минуты {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'

        return f'{num_time[m - m % 10]} {num_time[m % 10]} минуты {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'
    else:
        return f'{num_time[m - m % 10]} {num_time[m % 10]} минут {hour_sklan(h + 1) if h != 12 else hour_sklan(1)}'


def minute_more_or_equals45(h: int, m: int):
    if 60 - m == 1:
        return f'без {num_time[1][:2]}ной минуты {num_time[h + 1] if h != 12 else num_time[1]}'
    elif 60 - m == 2:
        return f'без {num_time[2][:2]}ух минут {num_time[h + 1] if h != 12 else num_time[1]}'
    elif 60 - m == 8:
        return f'без {num_time[8][:3]}ьми минут {num_time[h + 1] if h != 12 else num_time[1]}'
    elif 60 - m == 3 or 60 - m == 4:
        return f'без {num_time[60 - m][:-1]}ёх минут {num_time[h + 1] if h != 12 else num_time[1]}'
    else:
        return f'без {num_time[60 - m][:len(num_time[60 - m]) - 1]}и минут {num_time[h + 1] if h != 12 else num_time[1]}'


print(test_input_times(input("Please, enter the desired time in the format hh:mm: ")))
