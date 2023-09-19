import random

left_Border=int(input("Enter the left border: "))
right_Border=int(input("Enter the right border: "))

print(f"A random number in a range ({left_Border};{right_Border}):\n",random.randint(left_Border, right_Border))