word = 'alla'


def rec_is_polindrome(s: str):
    if len(s) == 0:
        print(f'Word is polindrome')
        return

    if s[0] == s[-1]:
        rec_is_polindrome(s[1:-1])
    else:
        print(f'Word is NOT a polindrome')


rec_is_polindrome(word)
