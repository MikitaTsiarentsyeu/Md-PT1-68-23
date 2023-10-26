def get_ranges(numbers):
    if not numbers:
        return ""

    ranges = []
    start = end = numbers[0]

    for num in numbers[1:]:
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

    return ", ".join(ranges)

numbers1 = [0, 1, 2, 3, 4, 7, 8, 10]
result1 = get_ranges(numbers1)
print(result1)  

numbers2 = [4, 7, 10]
result2 = get_ranges(numbers2)
print(result2)  

numbers3 = [2, 3, 8, 9]
result3 = get_ranges(numbers3)
print(result3)  
