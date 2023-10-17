import random

global_var = [5]

def test():
    x = random.randint(1, 10)
    print(x)
    # print(global_var)
    global_var.append("test")
    print(global_var)

    def inner():
        print(global_var)
    inner()

def a_test():
    x = "a_test"
    print(x)

test()
a_test()
test()

print(global_var)

for i in range(2):
    print(i)
print(i)

[t for t in range(10)]
print(t)