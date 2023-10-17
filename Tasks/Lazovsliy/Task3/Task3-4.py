def find_second_largest(numbers):
    # Check if the list has at least two elements
    if len(numbers) < 2:
        return "The list should have at least two numbers to find the second largest."
    
    # Initialize the largest and second largest variables
    largest = second_largest = float('-inf')
    
    # Iterate through the list of numbers
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    # Check if a second largest number was found
    if second_largest == float('-inf'):
        return "There is no second largest number in the list."
    
    return second_largest

# Prompt the user for input by taking a comma-separated list of numbers
input_str = input("Введите список чисел через запятую: ")

# Split the input string into a list of numbers
numbers = [int(x) for x in input_str.split(',')]

# Find the second largest number in the list
result = find_second_largest(numbers)

# Display the result
print("Второе по величине число в списке:", result)