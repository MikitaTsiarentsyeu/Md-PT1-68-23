user_input = input("Please enter a list of integer numbers, e.g. 1, 2, 3, etc.:\n")
user_input = user_input.replace(" ", "").split(",")
sum = 0

for i in user_input:
    if int(i) % 2 == 0:
        sum += int(i)

print(sum)