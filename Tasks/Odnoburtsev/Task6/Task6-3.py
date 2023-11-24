test_str = "The February TIOBE Index of the most popular programming languages is out, and while the work going on in the background of TIOBE calculations has changed, not much has shifted in the way of rankings."

char_desired = input("Please input a character you want to count:\n")

def char_counter(l: list, char: str):
    if not len(l):
        return 0
    if l[0] == char:
        return 1 + char_counter(l[1:], char)
    else:
        return char_counter(l[1:], char)
    
print(f"The string contains {char_counter(test_str, char_desired)} '{char_desired}' character")