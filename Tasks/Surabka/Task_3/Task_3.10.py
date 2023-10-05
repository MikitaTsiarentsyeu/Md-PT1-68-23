s = [18, 5, 7, 1, 2, 3, 4, 9, 16, 0, 19, 122]
prime = []

for i in s:
    counter = 0
    if i == 1 or i == 0:
        counter += 1
    for j in range (2, (i // 2 + 1)):
        if i % j == 0:
            counter += 1
    if counter == 0:
        prime.append(i)
print(prime)
