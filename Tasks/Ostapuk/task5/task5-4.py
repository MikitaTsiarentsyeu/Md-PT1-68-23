def count_letters(string):
    lowercase_count = 0
    uppercase_count = 0
    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
    return lowercase_count, uppercase_count
string = "grEEn Dog"
result = count_letters(string)
print(result)


