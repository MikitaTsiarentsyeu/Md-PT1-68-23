# The first method is very simple, using the string method ".swapcase")))
# test_string = "Write a program that takes a string as input and returns the \
# string with all capital letters converted to lowercase and vice versa."
# print(test_string.swapcase())

# Second method
test_string = "Write a program that takes a string as input and returns the \
string with all capital letters converted to lowercase and vice versa."
x = list(test_string.lower())
new_string = ""

for i in test_string:
    for j, symbol in enumerate(x):
        if i != symbol:
            new_string += x.pop(j)
            break
        else:
            new_string += (x.pop(j)).upper()
            break
print(new_string)