global_im = 5
global_m = []

def some_func(a):
    global_im = 6
    global_im += 2
    global_m.append(global_im)

    print(global_im)
    print(global_m)

    local_val = "test"
    print(a, local_val)

# some_func(1)
# print(global_im)
# print(global_m)

def outer():
    print("outer starts")

    outer_val = 5
    def inner():
        global_m.append(1)
        global global_im
        global_im = 10
        nonlocal outer_val
        outer_val = "test"

    inner()
    print(outer_val)
    print("outer ends")

    return inner

print(global_im)
new_func = outer()
new_func()
print(global_im)