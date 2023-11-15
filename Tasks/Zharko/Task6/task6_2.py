def palindrome(a):
    '''Recursive function to check whether a given string is a palindrome.'''
    if len(a) <= 1:
        return True
    if a[0] == a[-1]:
        return palindrome(a[1:-1])
    else:
        return False


string = "tenet tenet"
print(palindrome(string))


