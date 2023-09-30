user_input = input("Please enter a list of numbers, e.g. 1.0, 2, 3, etc.:\n")
user_input = user_input.replace(" ", "").split(",")

new_input = []

for k in user_input:
    new_input.append(float(k))

m = 0
for i in new_input:
    m += i

mean_value = m / len(new_input)
print(mean_value)