# 2. Write a program that takes a list of numbers as input and returns
# the sum of all even numbers in the list.

def sum_even_num(numbers):
    sum_even = 0
    for i in numbers:
        if i % 2 == 0:
            sum_even += i
    return f'The sum of all even numbers is equal: {sum_even}'


print(sum_even_num(map(int, input("Enter numbers separated by spaces:\n").split())))
