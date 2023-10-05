test_string = "Write a program that takes a string as input and returns a \
dictionary with the count of each word in the string."
test_list = test_string.replace(".", "").replace(",", "").split()
test_dict = {}

for i in test_list:
    x = 0
    for j in test_list:
        if i == j:
            x += 1
            test_dict[i] = x
print(test_dict)

