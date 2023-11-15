class Dog:

    __colors = ["white", "black", "mixed"]
    __default_color = __colors[0]

    def __init__(self, name, age=1, color=__default_color):
        self.name = name
        self.__set_age(age)
        if color not in Dog.__colors:
            self.color = Dog.__default_color
        else:
            self.color = color

    def get_age(self):
        if self.__age:
            return "bark!"*self.__age
        else:
            return ""

    # def get_age(self):
    #     return self.__age

    def __set_age(self, age):
        if isinstance(age, int) and age > 0: 
            self.__age = age
        else:
            self.__age = None

    def delete_age(self):
        self.__age = None
        

    age = property(get_age, __set_age)

d = Dog("Zefirka", 3, "red")
print(d.name, d.get_age(), d.color)

# d.name = "Zefirka"
# print(d.name)

# d.age = 10
# d.age = -10
# d.age = "three years"
d.get_age()

# print(Dog.__colors)
# Dog.__colors.pop(0)
# print(Dog.__colors)

# d.__age = 2

print(Dog.__dict__)

Dog.default_color = "blue"

print(Dog._Dog__colors)

print(d.get_age())

# d.__set_age("test")

print(d.get_age())

print(d.age)
d.age = 5
print(d.age)
