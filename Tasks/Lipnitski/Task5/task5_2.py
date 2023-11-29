l = ['Hello', 'world', 'How', 'are', 'you']


def list_string_reverse(list):
    reversed_list = []
    for word in list:
        reversed_list.append(word[::-1])
    return reversed_list


print(list_string_reverse(l))
