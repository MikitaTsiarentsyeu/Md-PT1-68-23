# First way ------------------------------------------------------------------|
# list_number = [126, 43, 400, 8, 14, 53, 200, 3, 97, 73, 8, 11, 12, 105]
# list_number.sort(reverse=True)
# print(list_number)
# print(list_number[1])
# ----------------------------------------------------------------------------|

# Second way -----------------------------------------------------------------|
# list_number = [126, 43, 400, 8, 14, 53, 200, 3, 97, 73, 8, 11, 12, 105]
# x = len(list_number)
# for i in range(x):
#     for j in range(i):
#         if list_number[i] > list_number[j]:
#             list_number[j], list_number[i] = list_number[i], list_number[j]
# print(list_number[1])
# ----------------------------------------------------------------------------|

# Third way-------------------------------------------------------------------|
list_number = [126, 43, 400, 8, 14, 53, 200, 3, 97, 73, 8, 11, 12, 105]
x = len(list_number)

for j in range(2):
    for i in range(x - 1):
        if list_number[i] > list_number[i + 1]:
            list_number[i], list_number[i + 1] = list_number[i + 1], list_number[i]
print(list_number[x - 2])
# ----------------------------------------------------------------------------|