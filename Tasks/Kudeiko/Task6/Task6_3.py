# 3. Write a recursive function to count the number of occurrences
# of a given character in a string.
class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class NullStringError(Error):
    """Вызывается когда строка пуста"""
    pass


def count_symb(string: str, symb, count=0):
    if symb not in string:
        return f"{count} '{symb}' in string"
    return count_symb(string[string.index(symb) + 1:], symb, count + 1)


string = input("Enter the string to be checked:\n")

while True:
    try:
        sym = input("Enter the symbol you are looking for:\n")
        if not sym:
            raise NullStringError("Symbol can't be null")
        break
    except NullStringError as e:
        print(e)
        continue
    except:
        continue

print(count_symb(string, sym))
