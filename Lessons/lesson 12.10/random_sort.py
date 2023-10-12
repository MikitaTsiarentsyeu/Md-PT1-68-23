import random

l = [3,5,67,7,54,3,2,3]

# for i in range(100):
#     i, j = random.randint(0, len(l)-1), random.randint(0, len(l)-1)
#     l[i],l[j] = l[j],l[i]
#     print(l)

def random_sort(l:list):
    "sorting a list in place"
    n = len(l)
    counter = 0
    while not is_sorted(l):
        i = generate_index(n)
        j = i
        while i == j:
            j = generate_index(n)
        swap(l, i, j)
        counter += 1
        print(counter)

def is_sorted(l:list)->bool:
    for i in range(len(l)-1):
        if l[i+1]<l[i]:
            return False
    return True

def generate_index(n):
    return random.randint(0, n-1)

def swap(l, i, j):
    l[i],l[j] = l[j],l[i]

random_sort(l)
print(l)