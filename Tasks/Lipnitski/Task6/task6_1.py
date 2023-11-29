str_to_reverse = 'Hi all people'


def rec_reverse_string(s: str):
    if len(s) == 0:
        return
    rec_reverse_string(s[1:])
    print(s[0], end='')


rec_reverse_string(str_to_reverse)
