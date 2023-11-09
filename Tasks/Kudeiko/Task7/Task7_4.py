# 4. Write a decorator function that logs the execution time, arguments and return value of a function to a file.
import random
import time


class Error(Exception):
    pass


class NumberLessThanOneError(Error):
    """"Вызывается когда значение менее 0"""
    pass


class NumberMoreThan10000Error(Error):
    """"Вызывается когда значение более 10000"""
    pass


def decorator(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        with open("Task7_4.txt", "a") as f:
            f.write(f'Time: {end - start}\nArguments: {args[0]}\nValue of a function: {res}\n')

    return wrapper


@decorator
def chance(n, count=0):
    """The function returns the number of iterations required to find a random
        integer equal to the entered one in the range from 0 to 10000"""
    while n != random.randint(0, 10000):
        count += 1
    return count


while True:
    try:
        number = int(input("Enter an integer in the range from 0 to 10000:\n"))
        if number < 0:
            raise NumberLessThanOneError("The entered number is less than 0!")
        elif number > 10000:
            raise NumberMoreThan10000Error("The number entered is greater than 10000!")
        break
    except ValueError:
        print("The character entered is not an integer!")
    except NumberLessThanOneError as e:
        print(e)
    except NumberMoreThan10000Error as e:
        print(e)

chance(number)
