
#Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

def sum_even_numbers(numbers):
    even_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
    return even_sum

input_numbers = input("Enter a list of numbers separated by a space: ").split()

numbers = [int(x) for x in input_numbers]

result = sum_even_numbers(numbers)
print(f"Sum of even numbers in the list: {result}")
