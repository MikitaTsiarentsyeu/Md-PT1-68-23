def function(a: list) -> str:
    l = []
    start = a[0]
    
    for i in range(len(a) - 1):
        if a[i] + 1 == a[i + 1]:
            continue
        elif a[i] == start:
            l.append(f"{a[i]}")
        else:
            l.append(f"{start}-{a[i]}")
        start = a[i + 1]
    
    if a[-2] + 1 == a[-1]:
        l.append(f"{start}-{a[-1]}")
    else:
        l.append(f"{start}")
    
    return ", ".join(l)

get_ranges_1 = [0, 1, 2, 3, 4, 6, 8, 9, 10]
get_ranges_2 = [4,7,10]
get_ranges_3 = [2, 3, 8, 9]

print(function(get_ranges_1))
print(function(get_ranges_2))
print(function(get_ranges_3))

