# 3. Write a function that takes a list of integers as input and returns the sum of all even numbers in the list.
# Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.


def sum_even_num(lst, total_amount=0):
    for i in lst:
        if i % 2 == 0:
            total_amount += i
    return total_amount


try:
    lst = list(map(int, input("Enter integers separated by spaces:\n").split()))
except ValueError:
    print("Invalid input type")
else:
    print(sum_even_num(lst))
