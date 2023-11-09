class Dog:
    """TEST DOG CLASS"""

    name = "Zefirka"
    color = "white"
    age = 3

    def bark():
        print("bark!")

    def bark_age(self):
        print("bark!"*self.age)

print(Dog.name, Dog.color, id(Dog))
# Dog.bark_age()

d = Dog()
print(d, type(d))
print(d.name, d.color)

Dog.name = "Max"
print(Dog.name, d.name)

d.name = "Good boy"
print(Dog.name, d.name)

Dog.name = "Maximum"
print(Dog.name, d.name)

d2 = Dog()
print(d2.name, d2.color)
d2.name = "test"
print(d2.name)

d.age = 5
d.bark_age()

print(Dog.__dict__)
print(d.__dict__)

d.color = "black"
print(d.__dict__)

d.test = "test"
print(d.test)
print(d.__dict__)

Dog.breed = "wss"
print(Dog.breed, d.breed)

# print.test = "test" monkey patching
# print(print.test)