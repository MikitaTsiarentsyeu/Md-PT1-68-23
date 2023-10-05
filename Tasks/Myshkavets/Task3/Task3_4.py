#Write a program that takes a list of numbers as input and returns the second largest number in the list.

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
second_largest = sorted(set(numbers))[-2]
print(second_largest)