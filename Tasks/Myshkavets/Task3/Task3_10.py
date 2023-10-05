#Write a program that takes a list of numbers as input and returns the largest prime number in the list

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
largest_prime = max(filter(is_prime, numbers), default=None)
print(largest_prime)