s = [15, 54, 2, 75, 6, 45, 64, 7]
largest_1 = 0
largest_2 = 0
for i in s:
    if i > largest_1:
        largest_2 = largest_1
        largest_1 = i
    elif i > largest_2:
        largest_2 = i
print(largest_2)


# s.sort(reverse=True)
# print(s[1])
