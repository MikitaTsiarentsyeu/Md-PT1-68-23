string = input("Enter the text: ").split()
new_string = []
for i in string:
    if len(i) > 5:
        new_string.append(i)
print(new_string)