# 3. Write a program that takes a string as input and returns
# a dictionary with the count of each word in the string.

def dict_count_of_word(string: str):
    lst_string = string.lower().split()
    count_world = {}
    for i in lst_string:
        if not i.isalpha():
            continue
        if i not in count_world:
            count_world.update({i: lst_string.count(i)})
    return count_world


print(dict_count_of_word(input("Enter your string:\n")))
