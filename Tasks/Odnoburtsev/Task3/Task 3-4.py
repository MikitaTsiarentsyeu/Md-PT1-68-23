user_input = input("Please enter a list of numbers, e.g. 1.0, 2, 3, etc.:\n")
user_input = user_input.replace(" ", "").split(",")

new_user_input = []
for k in user_input:
    new_user_input.append(int(k))

for i in range(len(new_user_input)-1):
    for j in range(len(new_user_input)-1):
        if new_user_input[j] > new_user_input[j+1]:
            new_user_input[j], new_user_input[j+1] = new_user_input[j+1], new_user_input[j]
            print(new_user_input)

print(new_user_input)
print(new_user_input[-2])