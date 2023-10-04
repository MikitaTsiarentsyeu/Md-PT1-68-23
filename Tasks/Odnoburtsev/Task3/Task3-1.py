while True:
    user_input = input("Please enter any phrase in English or Russian:\n")
    user_input = user_input.replace(" ", "")

    if user_input.isalpha() == False:
        print("Please don't use other symbols, except letters\n")
        continue
    
    break

def vowel_count(x):
    
    number_vowels = 0
    vowels = "aAeEiIuUoOyYаАоОиИеЕуУюЮыЫэЭяЯ"
    
    # The first option
    for i in x:
        if i in vowels:
            number_vowels += 1
    
    print(f"The number of vowels in the string you entered is {number_vowels}")

    # The second option
#     for i in user_input:
#         for j in vowels:
#             if i == j:
#                 number_vowels += 1
#     print(f"The number of vowels in the string you entered is {number_vowels}")

vowel_count(user_input)



    
