def sum_of_evens(numbers):
    if not isinstance(numbers, list):
        return "Invalid input type"

    sum_evens = 0
    try:
        for num in numbers:
            if not isinstance(num, int):
                raise TypeError
            if num % 2 == 0:
                sum_evens += num
    except TypeError:
        return "Invalid input type"

    return sum_evens

# Example usage: 
print(sum_of_evens([2, 5, 6, 8]))  # Should return 16 (which is 2 + 6 + 8)
print(sum_of_evens([1, 3, 5]))     # Should return 0 (no even numbers)
print(sum_of_evens("a string"))    # Should return "Invalid input type"
print(sum_of_evens([1, 2, 'a']))   # Should return "Invalid input type"