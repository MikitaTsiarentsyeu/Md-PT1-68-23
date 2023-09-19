# 5.Write a program that generates a random number in a given range,
# and shows the answer to a user, ask a user for the left and right border.

import random as r

border_l = int(input("Enter an integer for the left border: "))
border_r = int(input("Enter an integer for the right border: "))
if border_l <= border_r:
    print(f"Random number: {r.randint(border_l, border_r)}")
else:
    border_l, border_r = border_r, border_l
    print(f"Random number: {r.randint(border_l, border_r)}")

