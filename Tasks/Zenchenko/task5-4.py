def lu(x1):
    u = 0
    lo = 0
    for i in range(len(x1)):
        if x1[i].islower():
            lo += 1
        else:
            u += 1

    return lo, u


x = input("Enter string: ")
print("The  count of lower case letters:", lu(x)[0], "\nThe  count of upper case letters:", lu(x)[1])
