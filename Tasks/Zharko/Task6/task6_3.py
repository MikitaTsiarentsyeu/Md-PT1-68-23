def func(a, char, n = 0):
    '''Recursive function to count the number of occurrences of a given
    character in a string'''
    if not a:
        return 0
    if char == a[0].lower():
        n += 1
    return n + func(a[1:], char)


string = "Test string Test string"
print(f"Count character: {func(string, 't')}")

