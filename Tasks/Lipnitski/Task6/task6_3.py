test_string = 'How are you 12399999'


def get_count(s, char, counter=0):
    if len(s) == 0:
        return counter

    if s[0] == char:
        counter += 1
    return get_count(s[1:], char, counter)


print(get_count(test_string, 'H'))
