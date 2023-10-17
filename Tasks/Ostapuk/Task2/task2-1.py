t = input('Enter time in format hh:mm: ')
t_str = ''
nums_hour = {
    1: ['один', 'первого'],
    2: ['два', 'второго'],
    3: ['три', 'третьего'],
    4: ['четыре', 'четвертого'],
    5: ['пять', 'пятого'],
    6: ['шесть', 'шестого'],
    7: ['семь', 'седьмого'],
    8: ['восемь', 'восьмого'],
    9: ['девять', 'девятого'],
    10: ['десять', 'десятого'],
    11: ['одинадцать', 'одинадцатого'],
    12: ['двенадцать', 'двенадцатого'],
    13: ['один', 'первого'],
}
nums_min = {
    1: ['одна', 'одной'],
    2: ['две',  'двух'],
    3: ['три', 'трех'],
    4: ['четыре', 'четырех'],
    5: ['пять', 'пяти'],
    6: ['шесть', 'шести'],
    7: ['семь', 'семи'],
    8: ['восемь', 'восьми'],
    9: ['девять', 'девяти'],
    10: ['десять', 'десяти'],
    11: ['одинадцать', 'одинадцати'],
    12: ['двенадцать', 'двенадцати'],
    13: ['тринадцать', 'тринадцати'],
    14: ['четырнадцать', 'четырнадцати'],
    15: ['пятнадцать', 'пятнадцати'],
    16: ['шестнадцать', 'шестнадцати'],
    17: ['семнадцать', 'семнадцати'],
    18: ['восемнадцать', 'восемнадцати'],
    19: ['девятнадцать', 'девятнадцати'],
    20: ['двадцать', 'двадцати'],
    30: ['тридцать'],
    40: ['сорок'],
    50: ['пятьдесят'],
}
t_list = t.split(':')
hour, min = t_list
hour, min = int(hour), int(min)
if ':' not in t or t.count(':') != 1:
    print("You entered incorect data without a : symbol.")
    exit()

if len(t) != 5:
    print("You entered incorect time.")
    exit()

if hour < 0 or hour >= 24 or min < 0 or min >= 60:
    print("You entered incorect time.")
    exit()

if hour > 12:
    hour -= 12

if min == 0:
    if hour == 1:
        t_str = nums_hour[hour][0] + ' ' + 'час ровно'
    elif 1 < hour < 5:
        t_str = nums_hour[hour][0] + ' ' + 'часа ровно'
    else:
        t_str = nums_hour[hour][0] + ' ' + 'часов ровно'
elif min <= 20:
    if min == 1:
        t_str = nums_min[min][0] + ' ' + 'минута' + ' ' + nums_hour[hour + 1][1]
    elif 1 < min < 5:
        t_str = nums_min[min][0] + ' ' + 'минуты' + ' ' + nums_hour[hour + 1][1]
    else:
        t_str = nums_min[min][0] + ' ' + 'минут' + ' ' + nums_hour[hour + 1][1]
elif 20 < min < 30:
    if min - 30 == 1:
        t_str = nums_min[20][0] + ' ' + nums_min[min - 20][0] + ' ' + 'минута' + ' ' + nums_hour[hour + 1][1]
    elif 1 < min - 20 < 5:
        t_str = nums_min[20][0] + ' ' + nums_min[min - 20][0] + ' ' + 'минуты' + ' ' + nums_hour[hour + 1][1]
    else:
        t_str = nums_min[20][0] + ' ' + nums_min[min - 20][0] + ' ' + 'минут' + ' ' + nums_hour[hour + 1][1]
elif min == 30:
    t_str = 'половина' + ' ' + nums_hour[hour + 1][1]
elif 30 < min < 40:
    if min - 30 == 1:
        t_str = nums_min[30][0] + ' ' + nums_min[min - 30][0] + ' ' + 'минута' + ' ' + nums_hour[hour + 1][1]
    elif 1 < min - 30 < 5:
        t_str = nums_min[30][0] + ' ' + nums_min[min - 30][0] + ' ' + 'минуты' + ' ' + nums_hour[hour + 1][1]
    else:
        t_str = nums_min[30][0] + ' ' + nums_min[min - 30][0] + ' ' + 'минут' + ' ' + nums_hour[hour + 1][1]
elif 40 < min < 45:
    if min - 40 == 1:
        t_str = nums_min[40][0] + ' ' + nums_min[min - 40][0] + ' ' + 'минута' + ' ' + nums_hour[hour + 1][1]
    else:
        t_str = nums_min[40][0] + ' ' + nums_min[min - 40][0] + ' ' + 'минуты' + ' ' + nums_hour[hour + 1][1]
elif 45 <= min:
    if 60 - min == 1:
        t_str = 'без' + ' ' + nums_min[60 - min][1] + ' ' + 'минуты' + ' ' + nums_hour[hour + 1][1]
    else:
        t_str = 'без' + ' ' + nums_min[60 - min][1] + ' ' + 'минут' + ' ' + nums_hour[hour + 1][1]
print(t_str)