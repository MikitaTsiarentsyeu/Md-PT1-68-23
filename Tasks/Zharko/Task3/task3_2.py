list_number = [1, 43, 4, 8, 14, 5, 2, 3, 7, 8, 11, 12, 10]
sum = 0
for i in list_number:
    if i % 2 == 0:
        sum += i
print(f"Sum of all even numbers = {sum}")