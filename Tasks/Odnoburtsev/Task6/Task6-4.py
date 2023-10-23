import random
N = random.randint(0, 5)
pow = random.randint(0, 5)

def power(i):
    if isinstance(i, int):
        if i == 0:
            return 1
    return N*power(i-1)

print(f"The power {pow} of the number {N} is {power(pow)}")

