# 4. Write a recursive function to calculate the power of a given number.


def power(number: int, pow: int):
    if number == 0:
        return 0
    elif pow == 0 or number == 1:
        return 1
    elif pow == 1:
        return number
    elif pow > 1:
        return number * power(number, pow - 1)
    else:
        return 1 / number * power(number, pow + 1)

while True:
    try:
        number = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Please enter an integer: ")

while True:
    try:
        pow = int(input("Enter the power of the number: "))
        break
    except ValueError:
        print("Please enter an integer: ")

print(f"The number {number} to the power of {pow} is equal to: {power(number, pow)}")
