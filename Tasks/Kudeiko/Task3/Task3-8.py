# 8. Write a program that takes a list of numbers as input
# and returns the average of all numbers in the list.

def ave(lst):
    sum_n = 0
    for i in lst:
        sum_n += i
    return f"The average value is: {(sum_n / len(lst)):.2f}"


print(ave(list(map(int, input('Enter your number separated spaces:\n').split()))))
