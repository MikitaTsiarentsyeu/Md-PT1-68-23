# The first option
# import random
# def sum_values(a: int, b: int):
    # """Return a sum of random integers"""
#     print(f"The sum of {a} and {b} is equal to:")
#     return a + b

# print(sum_values(random.randint(1, 100), random.randint(1, 100)))

# The second option
first_input = input("Please enter the first integer:\n")
second_input = input("Please enter the second integer:\n")

def sum_values(x1, x2):
    """Validates data and returns a sum of integers entered by the user"""

    while True:
        try:            
            a, b = int(x1), int(x2)

        except ValueError:
            x1 = input("One of the value you entered was incorrect.\n\
Please enter the first integer again:\n")
            x2 = input("One of the value you entered was incorrect.\n\
Please enter the second integer again:\n")
            continue

        break

    print(f"The sum of numbers {a} and {b} is equal to")
    return a + b

print(sum_values(first_input, second_input))


