from functools import reduce

print((lambda x, y: x+y)(2, 3))

sum = lambda x, y: x+y

l = [2,4,6.5,'4',23,2,3,5.5,'6',7]
print(sorted(l, key=float))

test_str = "Abc Aac aaa aba"
print(sorted(test_str.split(), key=lambda x: x.lower()))

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l, key=lambda x: x[1]))

def sq(x):
    return x*x

l = [1,2,3,4,5,6,7,8,9]
print(list(map(sq, l)))
mp = map(lambda num: chr(num*10), l)
print([x for x in mp])

print([(lambda num: chr(num*10))(x) for x in l])

print(list(map(lambda num: chr(num*10), filter(lambda x: x % 2 == 0, l))))

print(reduce(lambda a, b: a+b, l))
print(reduce(lambda a, b: f"{a}-{b}", l))