lst_nums = [1, 2, 3, 4, 5, 6, 7]

lst_prime_nums = []

for num in lst_nums:
    if num == 1:
        continue
    count = 0
    for i in range(2, num // 2+1):
        if (num % i == 0):
            count += 1
    if count <= 0:
        lst_prime_nums.append(num)


print(max(lst_prime_nums))
