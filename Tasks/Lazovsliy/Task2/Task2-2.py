# Prompt the user for input in the specified format
user_input = input("Введите время в формате hh:mm ")

try:
    # Split the user input into hours and minutes
    hours, minutes = map(int, user_input.split(':'))

    # Define the Russian words for numbers
    hours_words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать"]
    minutes_words = ["", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать",
                      "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать",
                        "двадцать одна", "двадцать две", "двадцать три", "двадцать четыре", "двадцать пять", "двадцать шесть", "двадцать семь",
                          "двадцать восемь", "двадцать девять", "тридцать", "тридцать одна", "тридцать две"]
    
    # Define a function to handle different cases of minutes
    def get_minute_text(minutes):
        if minutes == 0:
            return "ровно"
        elif minutes < 30:
            return f"{minutes_words[minutes]} минут следующего часа"
        elif minutes == 30:
            return "половина"
        elif minutes > 30 and minutes < 45:
            return f"{minutes_words[60 - minutes]} минут следующего часа"
        elif minutes >= 45:
            return f"без {minutes_words[60 - minutes]} минут"

    # Construct the response based on the rules
    if minutes == 0:
        print(f"{hours_words[hours]} час {get_minute_text(minutes)}")
    else:
        print(f"{hours_words[hours]} часов {get_minute_text(minutes)}")

except ValueError:
    print("Неверный формат времени. Введите время в формате hh:mm.")