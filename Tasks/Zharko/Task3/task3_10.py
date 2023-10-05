list_number = [126, 43, 400, 8, 14, 53, 200, 3, 97, 73, 8, 11, 12, 105]
print(f"List: {list_number}")
list_number.sort(reverse=True)
for i in list_number:
    x = 0
    for j in range(1, i + 1):
        if i % j == 0:
           x += 1
    if x == 2:
        print(f"The largest prime number in the list: {i}")
        break

