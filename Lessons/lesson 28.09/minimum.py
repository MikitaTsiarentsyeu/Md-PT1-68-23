l = [3,43,564,56,67,45,23,23,23,1]

# print(min(l))
# print(sorted(l)[0])


min_i = 0
for i, e in enumerate(l):
    if e < l[min_i]:
        min_i = i

print(min_i, l[min_i])