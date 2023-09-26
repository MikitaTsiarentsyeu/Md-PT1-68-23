# d = {[1,2,3]:"test"} error

l = [1,2,3]

d = {(1,2,3):l}

print(d)

l.append(4)

print(d)

d[(1,2,3)].append(5)

print(l)


d = {1:"one", 2:"two", 3:"three"}

print(1 in d)
print(2 in d)
print(7 in d)
print("one" in d)
print("one" in d.values())
print(list(d.values()))
print(list(d.keys()))
print(list(d.items()))

# print(d[15]) error

key = 15
if key in d:
    print(d[key])

print(d.get(key))
print(d.get(key, "value not found"))
print(d.get(key, False))

res = d.get(key, False)
if res:
    print(res)

