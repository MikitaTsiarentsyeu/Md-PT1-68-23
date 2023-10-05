test_string = "Write a program that takes a string as input and returns the \
string reversed."
list_string = list(test_string)
x = len(list_string)
new_string = ""

for i in range(x - 1, -1, -1):
    new_string += list_string[i]
print(f"Old string - {test_string}")
print(f"String reversed - {new_string}")