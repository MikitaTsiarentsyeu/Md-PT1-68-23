def sum(a, b):
    print("hello from the sum function")
    result = a+b
    return result

res = sum(2, 3)
print(res)

# test_func() error

def test_func():
    print("it's a test")

test_func()

def level_2():
    print("it's level 2")

def level_1():
    print("it's level 1")
    level_2()

level_1()

new_func = level_2
new_func()
print(id(level_2), id(new_func))

def test_func(a, b, c):
    print(a, b, c)

test_func(1.0, "two", 3)

# def modify_int(a):
#     print(id(a))
#     a += 2
#     print(a)
#     print(id(a))

# test_int = 2
# print(id(test_int))
# modify_int(test_int)
# print(test_int)


def modify_list(a):
    print(id(a))
    a[0] += 2
    print(a)
    print(id(a))

test_int = [2]
print(id(test_int))
modify_list(test_int)
print(test_int)


for i in range(5):
    modify_list(test_int)
# modify_list(test_int)
# modify_list(test_int)
# modify_list(test_int)
# modify_list(test_int)

def test_counter(exec_count):
    print("exec number", exec_count)
    if exec_count:
        test_counter(exec_count-1)

test_counter(5)

def func_without_return():
    print("I will not return anything")

res = func_without_return()
print(res, type(res))

def test_return():
    print("a simple return")
    return

res = test_return()
print(res, type(res))

def name_a_number(number):
    if 0 <= number > 3:
        return
    if number == 1:
        return "one"
    elif number == 2:
        return "two"
    elif number == 3:
        return "three"
    
print(name_a_number(4))

def magic_return(a, b, c):
    return a, b, c

res = magic_return(1,2,3)
print(res)

i, j, k = magic_return(1,2,3)
print(i, j, k)

def sensless_return():
    return
    print("main function logic goes here")

sensless_return()