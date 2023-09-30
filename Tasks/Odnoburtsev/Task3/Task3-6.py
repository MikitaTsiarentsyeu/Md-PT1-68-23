user_input = input("Please enter a phrase:\n")

# user_input = "very long string obtained"
vowels = ["a", "A", "e", "E", "i", "I", "u", "U", "o", "O"]


new_input = ""
for i in user_input:
    if i not in vowels:
        new_input += i
        
print(new_input)
