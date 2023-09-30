user_input = input("Please enter a phrase:\n")

# user_input = "very long string obtained"

new_input = ''

for i in user_input:
    new_input = i + new_input

print(new_input)