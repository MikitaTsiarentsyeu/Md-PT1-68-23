def test_func(a, b):
    print(id(a), id(b))
    return a, b

x, y = 3, "test"
print(id(x), id(y))
test_func(x, y)

def evaluate(a, b="test", c=3.14):
    print(f"a={a}, b={b}, c={c}")
    return a*b+c

# evaluate(b=1,c=2,a=3)
evaluate(1, 2)

def fill(a, b, c, l=[]):
    l.append(a)
    l.append(b)
    l.append(c)
    return l


print(fill(1,2,3))
# l = [3,2,1]
# print(fill(1,2,3,l))
print(fill(1,2,3))
print(fill(1,2,3))
print(fill(1,2,3))

print(1,2,3,4,5,6,7,8,9)

def average(default=0, *args):
    if len(args) == 0:
        return default
    sum = 0
    for i in args:
        sum+=i
    return sum/len(args)

print(average(1,2,3,4,5,6,7,8,9,10))
print(average())

def my_print(*args, end="\n", sep=" "):
    print(*args, end=end, sep=sep)


def calling_pets(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{v} the {k}!")

calling_pets(cat="Kitty", dog="Barker")