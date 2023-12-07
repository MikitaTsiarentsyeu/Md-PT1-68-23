print(dir(str))
print(dir(int))
print(dir(object))

class Test:

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "this is only a test"
    
t = Test()
print(t)

print("test " + "str")
print("test ".__add__("str"))

# t+3

print("3" == 3)
print("3".__eq__(3))
print("the end")