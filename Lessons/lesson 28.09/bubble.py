l = [2,4,5,67,5,3,2,3,4,5,67,8,8]

for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]

    print(l)
