# 5. Write a recursive function to find the Nth number in the Fibonacci sequence.

class Error(Exception):
    pass


class NumberLessThanOneError(Error):
    """"Вызывается когда значение менее 1"""
    pass


def fibonachi(number: int, penult_n=0, last_n=1):
    if number == 1:
        return penult_n
    elif number == 2:
        return last_n
    elif number > 1:
        return fibonachi(number - 1, last_n, last_n + penult_n)


while True:
    try:
        number = int(input("Enter a number and find out what Fibonacci"
                           " number is hidden behind it: "))
        if number < 1:
            raise NumberLessThanOneError("Please enter an integer more than 1: ")
        break
    except ValueError:
        print("Please enter an integer: ")
        continue
    except NumberLessThanOneError as e:
        print(e)
        continue

print(f"In the Fibonacci sequence number {number} is the number {fibonachi(number)}")
