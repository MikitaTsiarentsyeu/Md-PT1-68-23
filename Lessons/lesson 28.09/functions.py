x = range(10)

print(list(x))

print(list(range(1, 101)))

string = "test str"
indexes = list(range(len(string)))

for i in indexes:
    print(string[i])

for i in range(1,101,5):
    print(i)

for i, e  in enumerate("some string"):
    print(i, e)

l = [[1,2,3], [4,5,6], [7,8,9]]
for i in l:
    for j in i:
        print(j)

l = [2,3,5,4,2,12,1,3,3,5]
without_ds = []
duplicates = []
for i in l:
    if i in without_ds:
        if i not in duplicates:
            duplicates.append(i)
    else:
        without_ds.append(i)

print(duplicates, without_ds)

duplicates_count = {}
for i in l:
    counter = -1
    for j in l:
        if i == j:
            counter += 1
    duplicates_count[i]=counter
print(duplicates_count)

for i in "abc":
    for j in "abc":
        for k in "abc":
            print(i, j, k)