
def list(a, b, c, l=[]):
    l.append(a)
    l.append(b)
    l.append(c)
    l.reverse()
    return l

print(list("one","two","three"))