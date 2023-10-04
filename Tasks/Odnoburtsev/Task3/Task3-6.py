user_input = input("Please enter a phrase:\n")

# user_input = "very long string obtained"

def vowel_removed(x):
    new_input = ""
    vowels = "aAeEiIuUoOyYаАоОиИеЕуУюЮыЫэЭяЯ"

    for i in x:
        if i not in vowels:
            new_input += i
        
    print(f"The string with all vowels removed {new_input}")

vowel_removed(user_input)

# List comprehension

# new_input = ""
# new_input = [new_input+i for i in user_input if i not in vowels]
# print(f"The string with all vowels removed {new_input}")
