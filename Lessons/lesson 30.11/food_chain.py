class Food:

    def __init__(self, name, f_type):
        self.name = name
        self.type = f_type

class Animal:

    def __init__(self, name) -> None:
        self.name = name

    def eat(self, something):
        print(f"{self.name}'s eating {something.name}")

    def phe(self):
        print("phe...")

class Carnivore(Animal):

    def eat(self, something):
        if something.type == "meat":
            Animal.eat(self, something)
        else:
            self.phe()

class Herbivore(Animal):

    def eat(self, something):
        if something.type == "herbal":
            Animal.eat(self, something)
        else:
            self.phe()

class Omnivore(Carnivore, Herbivore):

    def eat(self, something):
        if something.type == "meat":
            Carnivore.eat(self, something)
        elif something.type == "herbal":
            Herbivore.eat(self, something)
        else:
            self.phe()


stake = Food("stake", "meat")
grass = Food("grass", "herbal")

tigger = Carnivore('tigger')
cow = Herbivore('cow')
human = Omnivore('human')

print(Omnivore.__mro__)

class Dog:

    def eat(self, something):
        print(f"eating {something}")

def try_eat(animal, food):
    try:
        animal.eat(food)
    except AttributeError:
        print(f"{animal} is not Animal")

for a in tigger, cow, human, Dog(), "test":
    for f in stake, grass:
        try_eat(a, f)


5+6
print(int(5).__add__(6))
'5'+'6'
print('5'.__add__('6'))