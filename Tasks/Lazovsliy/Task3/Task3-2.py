def sum_even_numbers(numbers):
    # Initialize a variable to hold the sum of even numbers
    even_sum = 0
    
    # Iterate through the list of numbers
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    
    return even_sum

# Prompt the user for input by taking a comma-separated list of numbers
input_str = input("Введите список чисел через запятую: ")

# Split the input string into a list of numbers
numbers = [int(x) for x in input_str.split(',')]

# Calculate the sum of even numbers in the list
result = sum_even_numbers(numbers)

# Display the result
print("Сумма чётных чисел в списке:", result)