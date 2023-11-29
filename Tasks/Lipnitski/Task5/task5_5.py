def get_range_numbers(numbers):
    "a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers"
    ranges = []
    start = end = numbers[0]

    for n in numbers[1:]:
        if n == end + 1:
            end = n
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
            start = end = n

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")

    return ", ".join(ranges)


print(get_range_numbers([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_range_numbers([4, 7, 10]))
print(get_range_numbers([2, 3, 8, 9]))
