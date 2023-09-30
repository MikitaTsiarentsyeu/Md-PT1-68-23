user_input = input("Please enter a phrase:\n")

# user_input = "Very Long String Obtained"

new_input = ""
for i in user_input:
    # user_input = user_input.swapcase()
    if i == i.capitalize():
        new_input += i.lower()
    else:
        new_input += i.capitalize()

print(new_input)


