class Animal:

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("sleeping")

    def __str__(self):
        return f"Animal {self.name}"

class Dog(Animal):
    
    def __init__(self, name, color, breed, age=1):
        # self.name = name
        super().__init__(name)
        # Animal.__init__(self, name)
        self.breed = breed
        self.color = color
        self.age = age


d = Dog("Max", "black", "shepherd")
print(id(d))
print(d.name)

print(isinstance(Animal, object))
print(isinstance(Dog, object))
print(isinstance(d, object))


class RunningAnimal(Animal):

    def move(self):
        print("I'm running")

class SwimmingAnimal(Animal):

    def move(self):
        print("I'm swimming")

    def __str__(self):
        return f"swimming animal {self.name}"

class FlyingAnimal(Animal):

    def move(self):
        print("I'm flying")


class Croc(RunningAnimal, SwimmingAnimal): pass

c = Croc("croc")
c.move()
c.move()

class Duck(SwimmingAnimal, FlyingAnimal, RunningAnimal):

    def fly(self):
        FlyingAnimal.move(self)

    def swim(self):
        SwimmingAnimal.move(self)

    def run(self):
        RunningAnimal.move(self)


d = Duck("donald")
d.fly()
d.swim()
d.run()
d.move()

d.sleep()
print(d)

print(Duck.__mro__)

