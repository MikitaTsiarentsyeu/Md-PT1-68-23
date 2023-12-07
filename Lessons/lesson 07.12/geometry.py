import abc
import math

class Shape(abc.ABC):

    __supported_shapes = {}

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    @staticmethod
    def is_valid_value(value):
        return value > 0

    @classmethod
    def register_shape(cls, key, shape):
        cls.__supported_shapes[key] = shape

    @classmethod
    def create_square(cls, s):
        return cls.__supported_shapes['square'](s)
    
    @classmethod
    def create_circle(cls, r):
        return cls.__supported_shapes['circle'](r)
    
    @classmethod
    def create_shape(cls, key, *args):
        return cls.__supported_shapes[key](*args)


class Circle(Shape):

    def __init__(self, r):
        if Circle.is_valid_value(r):
            self.r = r
        else:
            raise ValueError(f"The value is invalid for {Circle.__name__}")

    def area(self):
        return math.pi * self.r ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.r
    

class Square(Shape):

    def __init__(self, s) -> None:
        if Square.is_valid_value(s):
            self.s = s
        else:
            raise ValueError(f"The value is invalid for {Square.__name__}")

    def area(self):
        return self.s ** 2
    
    def perimeter(self):
        return self.s * 4

c = Circle(2)
s = Square(2)

print(c.area(), c.perimeter())
print(s.area(), s.perimeter())

print(Shape.is_valid_value(5))

s.register_shape('square', Square)
s.register_shape('circle', Circle)

s = Shape.create_square(4)
print(s.area())

# c = Shape.create_circle(-2)

Shape.create_shape('circle', 2)