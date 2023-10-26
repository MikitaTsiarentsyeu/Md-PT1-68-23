def test_gen(n):
    n = n+1   
    yield n
    n += 1
    yield n
    n += 1
    yield n

# gen_obj = test_gen(1)
# for i in gen_obj:
#     print(i)

# for i in range(10):
#     pass

# gen1, gen2 = test_gen(1), test_gen(10)

# i_gen1, i_gen2 = iter(gen1), iter(gen2)

# while True:
#     try:
#         print(next(i_gen1), next(i_gen2))
#     except StopIteration:
#         break

def naive_range(start, finish, stride=1):
    res = [start]
    while True:
        start += stride
        if start >= finish:
            break
        res.append(start)
    return res

print(naive_range(0, 10))

for i in naive_range(0, 10):
    print(i)

def naive_range(start, finish, stride=1):
    while True:
        start += stride
        if start >= finish:
            break
        yield start

for i in naive_range(0, 10):
    print(i)


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        yield a
        count += 1
        if count == n:
            break
        a, b = b, a+b

print([i for i in fibonacci(100)])

l = [35634,23434,2,[3354543,223,556677,4],5444,34322,454]

def flat_sum(l):
    total = 0
    for i in l:
        if isinstance(i, list):
            total += flat_sum(i)
        else:
            total += i
    return total

print(flat_sum(l))

def flatten(l):
    for i in l:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i

for i in flatten([[[[1, []]]]]):
    print(i)


print([i for i in range(101)])
print({i for i in range(101)})
print(list((i for i in range(101))))

def genexp(n):
    i = 0
    while True:
        yield i
        i += 1
        if i >= n:
            break