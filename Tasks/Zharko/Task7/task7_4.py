import time

def decorator(func):
    def wrapper(a):
        start = time.time()
        func(a)
        end = time.time()
        res = end - start
        with open("task4.txt", "w") as f:
            f.write(f"Program execution time: {str(res)} seconds\n{str(a)}")
        return res    
    return wrapper

@decorator
def test(a):
    for i in range(1000):
        a.append(i)

l = []
print(test(l))
