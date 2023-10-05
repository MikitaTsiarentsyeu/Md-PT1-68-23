def is_prime(number):
    # Check if a number is prime
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_largest_prime(numbers):
    # Initialize a variable to hold the largest prime number found
    largest_prime = None
    
    # Iterate through the list of numbers
    for num in numbers:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    
    if largest_prime is not None:
        return largest_prime
    else:
        return "There are no prime numbers in the list."

# Prompt the user for input by taking a comma-separated list of numbers
input_str = input("Enter a list of numbers separated by commas: ")

# Split the input string into a list of numbers
numbers = [int(x) for x in input_str.split(',')]

# Find the largest prime number in the list
result = find_largest_prime(numbers)

# Display the result
print("The largest prime number in the list is:", result)