import math

class FreightTrain:

    cart_len = 10
    max_count = 25

    class TrainOverflowError(Exception):

        def __init__(self, overflow_count) -> None:
            self.overflow_count = overflow_count
            self.message = f"An overflow occured for the train, {self.overflow_count} is too big carts count"
            super().__init__(self.message)

    def __init__(self, cart_count):
        if cart_count > FreightTrain.max_count:
            raise FreightTrain.TrainOverflowError(cart_count)
        self.cart_count = cart_count

    def __str__(self):
        return f"I'm a train of {self.cart_count} carts!"
    
    def __int__(self):
        return self.cart_count
    
    def __len__(self):
        return self.cart_count*FreightTrain.cart_len
    
    def __add__(self, other):
        try:
            if isinstance(other, int):
                return FreightTrain(self.cart_count + other)
            return FreightTrain(self.cart_count + other.cart_count)
        except AttributeError:
            raise TypeError(f"unsupported operand type(s) for +: '{FreightTrain.__name__}' and '{type(other).__name__}'")

    def __eq__(self, other):
        try:
            return self.cart_count == other.cart_count
        except AttributeError:
            return False
        # if not isinstance(other, FreightTrain):
        #     return False
        
        # return self.cart_count == other.cart_count



train = FreightTrain(10)
print(train)

print(int(train))
print(len(train))

shorty = FreightTrain(2)
looooong = FreightTrain(25)
print(shorty+3)
print(shorty.__add__(3))
# print(3+shorty)
# print(int(3).__add__(shorty))

print(shorty == looooong)
# shorty.cart_count = 25
# print(shorty == looooong)

print(looooong == shorty)
print(3 == looooong)
print(int(3).__eq__(looooong))
print(looooong.__eq__(3))

try:
    print(looooong + shorty)
except FreightTrain.TrainOverflowError:
    print("overflow!")