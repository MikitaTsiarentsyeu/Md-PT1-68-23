cacheA = []
cacheB = []
cacheR = []


def dec1(a, b):

    def func(a1, b1):
        return int(a1)*int(b1)
    global cacheA
    global cacheB
    global cacheR
    if cacheA == a and cacheB == b:
        return cacheR
    else:
        cacheA = a
        cacheB = b
        cacheR = func(a, b)
        return cacheR


x = input("a")
y = input("b")
print(dec1(x, y))
print(dec1(x, y))
