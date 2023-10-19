
def apply(l, func):
    if not len(l):
        return
    elem = l[0]
    func(elem)
    apply(l[1:], func)

apply([1,2,3,4,5], print)

def print_sq(x):
    print(x*x)

apply([1,2,3,4,5], lambda x: print(x*x))