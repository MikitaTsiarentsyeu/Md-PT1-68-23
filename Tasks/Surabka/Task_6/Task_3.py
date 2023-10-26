def count(s, n, counter = 0):
    '''This recursive function counts the number of occurrences of a given character in a string'''
    if len(s) < 1:
        return counter
    if s[0] == n:
        counter += 1
    return count(s[1:], n, counter)
s = 'Write a recursive function 123323 %!%'
n = input()
print(count(s, n))