# count_dict = {}

# def counter(name, start=0):
#     if name not in count_dict:
#         count_dict[name]=start
#     count_dict[name] += 1
#     return count_dict[name]

# print(counter('100', 100))
# print(counter('100'))
# print(counter('100'))
# print(counter('100'))

# print(counter(10, 10))
# print(counter(10))
# print(counter(10))
# print(counter(10))

def counter(start=0):
    def action():
        nonlocal start
        start = start + 1
        return start

    return action

from_10 = counter(10)
from_100 = counter(100)

print(from_10())
print(from_10())
print(from_10())
print(from_10())

print(from_100())
print(from_100())
print(from_100())