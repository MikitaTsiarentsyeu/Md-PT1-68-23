s = {1,2,3,4,5}
print(type(s), s)

s = {}
print(type(s), s)

s = set()
print(type(s), s)

s = {1,1,1,2,3,4,3,2,12,1,1,2,3,4,5,6,7,7,3,5,3,3,2,34,3,5}
print(s)

s = set("test str")
print(s)

l1 = [1,2,3]
l2 = [3,2,1]
print(l1==l2)

print(set(l1)==set(l2))

test_obj = [1,1,1,1,1,2,2,2,2,3,3,3]
test_obj = list(set(test_obj))
print(test_obj)

print({1,2,3}.union({3,4,5}))
print({1,2,3}.intersection({3,4,5}))

s.add(2)
s.add(2)
s.add(2)
print(s)

s.remove(' ')
print(s)

# s.add([])

s.clear()
print(s)
