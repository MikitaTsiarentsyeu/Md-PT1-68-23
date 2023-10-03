print([x for x in range(10)])

l = []
for x in range(10):
    l.append(x)
print(l)

print([x*x for x in range(10)])

l = []
for x in range(10):
    l.append(x*x)
print(l)

l = [x*x for x in range(10) if x>5 or x == 3]
print(l)

l = []
for x in range(10):
    if x>5 or x == 3:
        l.append(x*x)
print(l)

s = "abc"
t = (1,2,3,4,5)

l = [letter+str(number) for letter in s for number in t]
print(l)

l = [[1,2,3], [4,5,6], [7,8,9]]
l = {y for x in l for y in x}
print(l)

d = {x:str(x) for x in range(5)}
print(d)