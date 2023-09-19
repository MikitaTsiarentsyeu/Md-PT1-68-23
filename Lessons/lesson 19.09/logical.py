x = True
y = False

print(x, y)

print(type(x), type(y))

print(isinstance(True, int))
print(isinstance(True, bool))
print(isinstance(True, str))
print(isinstance(True, float))

print((True+5)*False)

print(bool(45), bool(0.0), bool(-8), bool(0.0000000000001))
print(bool(""), bool([]))

res = print("test value")
print(res, type(res))
print(bool(res))

print(id(True), id(1))
print(True == 1)
print(id(True) == id(1))

print(not not not "")
print(not 88)

x = "value"
y = "test"
print(x or y)

print("left") or print("right")

