def mult(a, b): 
    return a*b

print(mult(2, 2))
print(mult(2, 2.0))
print(mult(2, "2"))


# print(mult(2, print)) error

def times_for_int(a:int, b:int):
    "this function will multiply only int values"
    if isinstance(a, int) and isinstance(b, int):
        return a*b
    # return "0"

times_for_int("test", 3)

def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

print(eq(("1", "2", "3"), "12333"))

def sum_2(a, b):
    return a+b

def sum_3(a, b, c):
    return sum(a, sum(b, c))

4+4
"test"+"test"

int(4).__add__(4)
"test".__add__("test")