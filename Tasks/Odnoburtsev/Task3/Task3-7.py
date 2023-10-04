user_input = input("Please enter a phrase:\n")
# user_input = "Very Long String Obtained"

# The simplest way to solve the task:
# user_input = user_input.swapcase()
# print(f"The string with all capital letters converted {user_input}")

def swap_letter(x):
    new_input = ""
    for i in x:
        if i == i.capitalize():
            new_input += i.lower()
        else:
            new_input += i.capitalize()

    print(f"The string with all capital letters converted {new_input}")

swap_letter(user_input)




