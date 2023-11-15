class BaseClass:

    def __init__(self, test) -> None:
        self.test = test

    attribute = "test"

    def method(self):
        print("doing something")

class ChildClass(BaseClass): pass

cc = ChildClass("test")
print(cc.attribute)
cc.method()