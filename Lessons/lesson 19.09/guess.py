import random
my_number = random.randint(0, 10)
your_number = int(input("Guess a number from 0 to 10:\n"))
if your_number == my_number:
    print("Lucky guess!")
else:
    print("Loooooser!")

# if your_number != my_number:
#     print("Loooooser!")
# else:
#     print("Lucky guess!")