numbers = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
}

def time_to_words(time_str):
    try:
        hh, mm = map(int, time_str.split(':'))
        
        if hh < 0 or hh > 23 or mm < 0 or mm > 59:
            return "Неверный формат времени"
        
        if mm == 0:
            return f"({numbers[hh]} часов ровно)"
        
        if mm <= 30:
            if mm == 15:
                return f"(четверть {numbers[hh]})"
            if mm == 30:
                return f"(половина {numbers[hh]})"
            if mm <= 20:
                return f"(без {numbers[mm]} минут {numbers[hh + 1]})"
            else:
                return f"(без {numbers[20]} {numbers[mm - 20]} минут {numbers[hh + 1]})"
        
        if mm > 30:
            mm = 60 - mm
            hh = (hh + 1) % 12
            if mm == 15:
                return f"(четверть {numbers[hh + 1]})"
            if mm <= 20:
                return f"(без {numbers[mm]} минут {numbers[hh]} )"
            else:
                return f"(без {numbers[20]} {numbers[mm - 20]} минут {numbers[hh]})"
    
    except ValueError:
        return "Неверный формат времени"

time_input = input("Введите время в формате hh:mm: ")

result = time_to_words(time_input)
print(result)