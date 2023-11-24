def reversed(a:str)->str:
    '''Recursive function to reverse a string'''
    if len(a) == 0:
        return a
    else:
        return reversed(a[1:]) + a[0]

string = "Test string"
print(reversed(string))