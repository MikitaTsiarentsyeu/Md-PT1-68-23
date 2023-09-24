time = input("Enter please time in the format hh:mm: ")
time = time.strip()

if time.count(":") == 1 and len(time) == 5:
    time = time.split(":")
    hour, min = int(time[0]), int(time[1])
    if hour > 23 or min > 59:
        print("Incorrect input, please try again!")
        input("Press enter to the end programm")
else:
    print("Incorrect input, please try again!")
    input("Press enter to the end programm")


dicthour = {
    0:["двенадцать", "двенадцатого"], 1:["один", "первого"],
    2:["два", "второго", "двух"], 3:["три", "третьего", "трёх"],
    4:["четыре", "четвёртого", "четырёх"], 5:["пять", "пятого"],
    6:["шесть", "шестого"], 7:["семь", "седьмого"], 8:["восемь", "восьмого"],
    9:["девять", "девятого"], 10:["десять", "десятого"],
    11:["одиннадцать", "одиннадцатого"], 12:["двенадцать", "двенадцатого"],
    13:["один", "первого"], 14:["два", "второго"], 15:["три", "третьего"],
    16:["четыре", "четвёртого"], 17:["пять", "пятого"],
    18:["шесть", "шестого"], 19:["семь", "седьмого"], 
    20:["восемь", "восьмого"], 21:["девять", "девятого"],
    22:["десять", "десятого"], 23:["одиннадцать", "одиннадцатого"],
    24:["двенадцать", "двенадцатого"]
}
dictmin = {
    0:"", 1:"одна", 2:"две", 3:"три", 4:"четыре", 13:"тринадцать ",
    14:"четырнадцать ", 15:"пятнадцать ", 16:"шестнадцать ", 17:"семнадцать ",
    18:"восемнадцать ", 19:"девятнадцать ", 20:"двадцать ", 30:"тридцать ",
    40:"сорок "
}

if min == 00:
    if hour == 0 or 5 <= hour <= 12 or 17 <= hour <= 23:
        print(f"{dicthour[hour][0]} часов ровно")
    elif hour == 1 or hour == 13:
        print(f"{dicthour[hour][0]} час ровно")
    else:
        print(f"{dicthour[hour][0]} часа ровно")
elif min == 30:
    print(f"Пол {dicthour[hour+1][1]}")
elif min < 45 and min != 30:
    if min == 1 or min == 21 or min == 31 or min == 41:
        print(f"{dictmin[min-1]}одна минута {dicthour[hour+1][1]}")
    elif 2 <= min <= 4 or 22 <= min <= 24 or 32 <= min <= 34 or 42 <= min <= 44:
        print(f"{dictmin[min - min % 10]}{dictmin[min % 10]} минуты \
{dicthour[hour+1][1]}")
    elif 10 <= min <= 12:
        print(f"{dicthour[min][0]} минут {dicthour[hour+1][1]}")
    elif 13 <= min <= 20:
        print(f"{dictmin[min]}минут {dicthour[hour+1][1]}")
    else:
        print(f"{dictmin[min - min % 10]}{dicthour[min % 10][0]} минут \
{dicthour[hour+1][1]}")
else:
    if 45 <= min <= 47:
        if hour == 0 or hour == 12:
            print(f"Без {(dictmin[60 - min]).replace('ь ', 'и')} минут час")
        else:    
            print(f"Без {(dictmin[60 - min]).replace('ь ', 'и')} минут \
{dicthour[hour+1][0]}")
    elif min == 59:
        if hour == 0 or hour == 12:
            print("Без одной минуты час")
        else:
            print(f"Без одной минуты {dicthour[hour+1][0]}")
    elif 48 <= min <= 55:
        if hour == 0 or hour == 12:
            print(f"Без {(dicthour[60 - min][0]).replace('ь', 'и')} минут час")
        else:
            print(f"Без {(dicthour[60 - min][0]).replace('ь', 'и')} минут \
{dicthour[hour+1][0]}")
    else:
        if hour == 0 or hour == 12:
            print(f"Без {dicthour[60 - min][2]} минут час")
        else:
            print(f"Без {dicthour[60 - min][2]} минут {dicthour[hour+1][0]}")

input("Press enter to the end programm")
