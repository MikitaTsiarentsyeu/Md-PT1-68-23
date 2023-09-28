#This file contains two solutions of the presented task.
#The main solution is based on the ternary if. Sorry for the long lines but I
#couldn't find the way to separate the if statement and move the rest
#to the next line. The second solution is based on the typical if statement.

time = input("Please enter the time in the 24-hour format, e.g. hh:mm\n")

if ":" not in time:
    print("Please enter the time using correct format")
    exit()

if len(time) != 5:
    print("Please enter the time using correct format")
    exit()

time = time.split(":")
hour, minute = int(time[0]), int(time[1])

if (hour < 0) | (hour > 23) | (minute < 0) | (minute > 59):
    print("Please enter correct values")
    exit()

if hour >= 12:
    hour = hour - 12

a = {
    1:("одна", "первого"),
    2:("две", "второго"),
    3:("три", "третьего"),
    4:("четыре", "четвертого"),
    5:("пять", "пятого"),
    6:("шесть", "шестого"),
    7:("семь", "седьмого"),
    8:("восемь", "восьмого"),
    9:("девять", "девятого"),
    10:("десять", "десятого"),
    11:("одиннадцать", "одиннадцатого"),
    12:("двенадцать", "двенадцатого"),
    13:("тринадцать", ""),
    14:("четырнадцать", ""),
    15:("пятнадцать", ""),
    16:("шестнадцать", ""),
    17:("семнадцать", ""),
    18:("восемнадцать", ""),
    19:("девятнадцать", ""),
    20:("двадцать", ""),
    30:("тридцать", ""),
    40:("сорок", ""),
    "hh":("час"),
    # "mm":("минута")
    }

if minute == 0:
    if hour == 0:
        print(f"{a[hour+12][0].capitalize()} {a['hh']}ов ровно")
    elif hour == 1:
        print(f"{a[hour][0].replace('на', 'ин').capitalize()} {a['hh']} ровно")
    elif hour == 2:
        print(f"{a[hour][0].replace('е', 'а').capitalize()} {a['hh']}а ровно")
    elif 3 <= hour <= 4:
        print(f"{a[hour][0].capitalize()} {a['hh']}а ровно")
    else:
        print(f"{a[hour][0].capitalize()} {a['hh']}ов ровно")
    
elif 1 <= minute <= 20:
    print(f"{a[minute][0].capitalize()} \
{''.join('минута' if char=='одна' else 'минуты' if char=='две' or char=='три' or char=='четыре' else 'минут' for char in a[minute][0:1])} \
{a[hour+1][1]}")
 
# elif minute == 1:
#     print(f"{a[minute][0]} {a['mm']} {a[hour+1][1]}")
# elif minute == 2:
#     print(f"{a[minute][0]} {a['mm'].replace('а','ы')} {a[hour+1][1]}")
# elif 3 <= minute <= 4:
#     print(f"{a[minute][0]} {a['mm'].replace('а','ы')} {a[hour+1][1]}")
# elif (5 <= minute <= 19) | (minute == 40):
#     print(f"{a[minute][0]} {a['mm'].replace('та','т')} {a[hour+1][1]}")
# elif minute == 20:
#     print(f"{a[minute//10][0]}дцать {a['mm'].replace('та','т')} {a[hour+1][1]}")

elif (21 <= minute <= 44) and (minute != 30):
    (print(f"{a[minute-minute%10][0].capitalize()} {a[minute%10][0]} \
{''.join('минута' if char == 'одна' else 'минуты' if char=='две' or char=='три' or char=='четыре' else 'минут' for char in a[minute%10][:1])} \
{a[hour+1][1]}"))
elif minute == 30:
    print(f"Половина {a[hour+1][1]}")

# elif minute == 21 | minute == 31:
#     print(f"{a[minute//10][0]}дцать {a[minute%10][0]} {a['mm']} {a[hour+1][1]}")
# elif minute == 22 | minute == 32:
#     print(f"{a[minute//10][0]}дцать {a[minute%10][0]} {a['mm'].replace('а','ы')} {a[hour+1][1]}")
# elif (23 <= minute <= 24) | (33 <= minute <= 34):
#     print(f"{a[minute//10][0]}дцать {a[minute%10][0]} {a['mm'].replace('а','ы')} {a[hour+1][1]}")
# elif (25 <= minute <= 29) | (35 <= minute <= 39):
#     print(f"{a[minute//10][0]}дцать {a[minute%10][0]} {a['mm'].replace('та','т')} {a[hour+1][1]}")
# elif minute == 41:
#     print(f"{a[minute-minute%10][0]} {a[minute%10][0]} {a['mm']} {a[hour+1][1]}")
# elif 42 <= minute <= 44:
#     print(f"{a[minute-minute%10][0]} {a[minute%10][0]} {a['mm'].replace('а','ы')} {a[hour+1][1]}")

elif (45 <= minute <= 59) and (minute != 52):
    if hour == 0:
        print(f"Без {''.join('одной минуты' if char == 'одна' else 'двух минут' if char == 'две' else 'трех минут' if char == 'три' else 'четырех минут' if char == 'четыре' else char[:-1]+'и минут' for char in a[60-minute][:1])} \
{a['hh']}")
    elif hour == 1:
        print(f"Без {''.join('одной минуты' if char == 'одна' else 'двух минут' if char == 'две' else 'трех минут' if char == 'три' else 'четырех минут' if char == 'четыре' else char[:-1]+'и минут' for char in a[60-minute][:1])} \
{a[hour+1][0][:-1]}а")
    else:
        print(f"Без {''.join('одной минуты' if char == 'одна' else 'двух минут' if char == 'две' else 'трех минут' if char == 'три' else 'четырех минут' if char == 'четыре' else char[:-1]+'и минут' for char in a[60-minute][:1])} \
{a[hour+1][0]}")
elif minute == 52:
    if hour == 0:
        print(f"Без {a[60-minute][0][:-3]}ьми минут {a['hh']}")
    elif hour == 1:
        print(f"Без {a[60-minute][0][:-3]}ьми минут {a[hour+1][0][:-1]}а")
    else:
        print(f"Без {a[60-minute][0][:-3]}ьми минут {a[hour+1][0]}")

#     if hour == 0:
#         print(f"Без {a[(60 - minute)][0][:-1]}и {a['mm'].replace('та','т')} {a['hh']}")
#     else:
#         print(f"Без {a[(60 - minute)][0][:-1]}и {a['mm'].replace('та','т')} {a[hour+1][1]}")
# elif minute == 52:
#     if hour == 0:
#         print(f"Без {a[(60 - minute)][0][:-3]}ьми {a['mm'].replace('та','т')} {a['hh']}")
#     else:
#         print(f"Без {a[(60 - minute)][0][:-3]}ьми {a['mm'].replace('та','т')} {a[hour+1][1]}")   
# elif 56 <= minute <= 57:
#     if hour == 0:
#         print(f"Без {a[60 - minute][0][:-1]}ех {a['mm'].replace('та','т')} {a['hh']}")
#     else:
#         print(f"Без {a[60 - minute][0][:-1]}ех {a['mm'].replace('та','т')} {a[hour+1][1]}")
# elif minute == 58:
#     if hour == 0:
#         print(f"Без {a[60 - minute][0][:-1]}ух {a['mm'].replace('та','т')} {a['hh']}")
#     else:
#         print(f"Без {a[60 - minute][0][:-1]}ух {a['mm'].replace('та','т')} {a[hour+1][1]}")
# else:
#     if hour == 0:
#         print(f"Без {a[60 - minute][0][:-1]}ой {a['mm'].replace('а','ы')} {a['hh']}")
#     else:
#         print(f"Без {a[60 - minute][0][:-1]}ой {a['mm'].replace('а','ы')} {a[hour+1][1]}")