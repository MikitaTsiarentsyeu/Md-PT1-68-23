def sum_of_even_numbers(input_list):
    if not isinstance(input_list, list) or not all(isinstance(num, int) for num in input_list):
        return "Invalid input type"

    even_sum = sum(num for num in input_list if num % 2 == 0)
    return even_sum

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = sum_of_even_numbers(numbers_list)
print(result)
