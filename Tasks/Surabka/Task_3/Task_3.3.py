s = 'Program returns a dictionary, Program returns'
s = s.split()

d = {}
for i in s:
    counter = 0
    for j in s:
        if i == j:
            counter += 1
    d[i] = counter
print(d)