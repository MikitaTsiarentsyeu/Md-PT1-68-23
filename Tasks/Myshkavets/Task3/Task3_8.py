#Write a program that takes a list of numbers as input and returns the average of all numbers in the list.

numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
average = sum(numbers) / len(numbers)
print(average)