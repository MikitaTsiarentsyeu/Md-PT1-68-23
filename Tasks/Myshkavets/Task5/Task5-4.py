
input_string = "Python continues to sit atop the index, with C and Java directly behind it. In Feb. 2022 those three also occupied the top spot, but with Python in the number three position, C at top, and Java in second place"
lower_count = sum(1 for char in input_string if char.islower())
upper_count = sum(1 for char in input_string if char.isupper())

print(f"Lowercase letters: {lower_count}")
print(f"Uppercase letters: {upper_count}")