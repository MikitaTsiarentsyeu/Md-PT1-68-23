# Function to generate a random number in a given range

import random
left_border = int(input("Enter left border: "))
right_border = int(input("Enter right border: "))

if left_border > right_border:
    left_border, right_border = right_border, left_border

random_num = random.randint(left_border, right_border)

print(f"Random number between {left_border} and {right_border} is: {random_num}")