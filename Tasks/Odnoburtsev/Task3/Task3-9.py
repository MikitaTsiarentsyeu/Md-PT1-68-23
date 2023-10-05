user_input = input("Please enter a phrase:\n")
# user_input = "very long string reversed"

def string_converter(x):
    new_input = ''

    for i in x:
        new_input = i + new_input

    print(f"The reversed phrase is {new_input}")

string_converter(user_input)