l = ['Hello!', 'world', 'How', 'are', 'you', 'lessons']


def give_word(list):
    'a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5'
    new_list = []
    for word in list:
        print(len(word))
        if len(word) > 5:
            new_list.append(word)
    return new_list


print(give_word(l))
