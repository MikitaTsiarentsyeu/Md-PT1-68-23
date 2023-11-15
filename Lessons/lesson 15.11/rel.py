class Engine:

    def __init__(self, vol, power):
        self.vol = vol
        self.pow = power

class SerialCar:

    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def get_make(self): pass

    def get_model(self): pass

    def get_engine(self):
        return self.engine

    def set_engine(self, engine):
        self.engine = engine

v3 = Engine(3.0, 155)

vw = SerialCar("vw", "polo", v3)

vw.set_engine(Engine(2.0, '100'))



class SuperCar:

    # class Engine:

    #     def __init__(self, vol, power):
    #         self.vol = vol
    #         self.pow = power

    def __init__(self, make, model, vol, power) -> None:
        self.make = make
        self.model = model
        self.engine = Engine(vol, power)

    def get_make(self): pass

    def get_model(self): pass

    def get_vol(self): pass

    def get_power(self): pass


ferrari = SuperCar("ferrari", "la ferrari", 6.0, 256)