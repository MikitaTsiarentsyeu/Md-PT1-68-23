def get_ranges(number_list):
    ranges = []
    start = number_list[0]
    end = number_list[0]

    for num in number_list[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
            start = end = num

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")

    return ', '.join(ranges)

# Example usage:
numbers1 = [0, 1, 2, 3, 4, 7, 8, 10]
numbers2 = [4, 7, 10]
numbers3 = [2, 3, 8, 9]

print(get_ranges(numbers1))  # Output: "0-4, 7-8, 10"
print(get_ranges(numbers2))  # Output: "4, 7, 10"
print(get_ranges(numbers3))  # Output: "2-3, 8-9"