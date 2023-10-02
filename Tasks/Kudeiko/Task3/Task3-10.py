# 10. Write a program that takes a list of numbers as input
# and returns the largest prime number in the list.

def prime(lst: list):
    prime_num = []
    for i in lst:
        if i == 1:
            continue
        if i == 2:
            prime_num.append(i)
            continue
        if all(i % j != 0 for j in range(2, int(round(i ** 0.5)) + 1)):
            prime_num.append(i)
    return max_prime(prime_num)


def max_prime(prime_num: list):
    for i in range(len(prime_num)):
        min_n = i
        for j in range(i + 1, len(prime_num)):
            if min_n < j:
                min_n = j
            prime_num[min_n], prime_num[i] = prime_num[i], prime_num[min_n]

    return prime_num[-1]


print(prime(list(map(int, input("Enter number separated spaces:\n").split()))))
