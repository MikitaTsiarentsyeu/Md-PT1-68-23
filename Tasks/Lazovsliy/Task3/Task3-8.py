def calculate_average(numbers):
    # Check if the list is not empty
    if not numbers:
        return "The list is empty. Cannot calculate average."
    
    # Calculate the sum of numbers in the list
    total_sum = sum(numbers)
    
    # Calculate the average
    average = total_sum / len(numbers)
    
    return average

# Prompt the user for input by taking a comma-separated list of numbers
input_str = input("Введите список чисел через запятую: ")

# Split the input string into a list of numbers
numbers = [float(x) for x in input_str.split(',')]

# Calculate the average of numbers in the list
result = calculate_average(numbers)

# Display the result
print("Среднее значение чисел в списке:", result)