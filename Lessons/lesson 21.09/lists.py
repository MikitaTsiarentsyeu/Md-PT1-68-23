l = []
print(type(l), l)

l = [1,2,3,4,5,6,7.0,"test"]
print(repr(l), repr(str(l)))

print(len(l))

print(l[0], l[-1])
# l[546] error

print(l[2:5])
print(l[::-1])

print([1,2,3]+[4,5,6])
print(list("test")+list(" str"))
print([0]*8)

l[0] = 1.0
print(l)

l[7:8] = list("test str")
print(l)

l.append("new elem")
print(l)

l.insert(0, "new first elem")
print(l)

l.extend("5646846846")
print(l)

l.remove('t')
print(l)

val = "test"
if val in l:
    l.remove(val)
    print(l)

print(l.pop())
print(l)

print(l.pop(0))
print(l)

del l[0]
print(l)

del l[2:8]
print(l)

del l
print(l)