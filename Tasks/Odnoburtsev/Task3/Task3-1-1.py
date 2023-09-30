user_input = input("Please enter any phrase:\n")
vowels = ["a", "A", "e", "E", "i", "I", "u", "U", "o", "O"]


def vowel_count(x):
    
    number_vowels = 0
    
    # The first option
    # for i in x:
    #     if i in vowels:
    #         number_vowels += 1
    
    # print(number_vowels)

    # The second option
    for i in user_input:
        for j in vowels:
            if i == j:
                number_vowels += 1
    print(number_vowels)

vowel_count(user_input)
    
