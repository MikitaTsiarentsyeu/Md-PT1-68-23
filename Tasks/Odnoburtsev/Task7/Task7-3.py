import random
from functools import reduce

# test_list = [1, 4, 3.5, 10, 7, 8, "f", 12, 11]
# test_list = ["rghfhgfh"]
test_list = random.sample(range(20), 7)

def list_checker(l: list):
    """Takes a list of integers as input and returns the sum of all even numbers in the list.
    If the input is not a list or not every element is int returns an error 'TypeError'"""
    print(l)
    while True:
        try:
            if isinstance(l, list):
                for x in l:
                    if not isinstance(x, int):
                        raise TypeError("Invalid input type")
                sum_even_numbers = reduce(lambda a, b: a+b, filter(lambda x: x % 2 == 0, l))
                print(f"The sum of all even numbers in the list is {sum_even_numbers}")
            else:
                raise TypeError("Invalid input type")
        except TypeError as e:
            print(e)
        break

list_checker(test_list)


            