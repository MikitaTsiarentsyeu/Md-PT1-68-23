list_number = [1, 43, 4, 8, 14, 5, 2, 3, 7, 8, 11, 12, 10]
sum = 0
for i in list_number:
    sum += i

result = sum / len(list_number) 
print(f"The average of all numbers - {result}")