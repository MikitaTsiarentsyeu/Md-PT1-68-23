import time


def decorator():
    start = time.time()

    def func():
        for i in range(0, 100000):
            print(i)
        return time.time()
    end = func()
    result = end - start
    with open("text1.txt", "w") as f1:
        f1.write(str(result))
    return result


print(decorator())
