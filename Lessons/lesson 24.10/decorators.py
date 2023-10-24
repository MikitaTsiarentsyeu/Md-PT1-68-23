import time

def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

def comment_process(func):
    def wrapper():
        print("starting of the function")
        func()
        print("the end of the function")
    return wrapper

@comment_process
@do_twice
def test_func():
    print("this is only a test")

# f = do_twice(test_func)
# f()

# test_func = do_twice(test_func)
test_func()


def check_rights(func):
    def wrapper(user):
        if "submit" in user:
            if user["submit"]:
                func(user)
        else:
            print("you have no access to that functionality")
    return wrapper

@check_rights
def submit_value(user):
    print(f"the user {user['name']} submitted a new value")

usr = {"name":"test_user", "submit":True}

submit_value(usr)

def time_it(func):
    def wrapper(n):
        start = time.time()
        res = func(n)
        finish = time.time()
        print(finish-start)
        return res
    return wrapper

@time_it
def load(n):
    return [i for i in range(n)]

r = load(100000)
print(r)

def wr(func):
    func()
    func()
    return func

def test_():
    print("122121212")

test_ = wr(test_)
test_()