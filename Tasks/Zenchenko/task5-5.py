def m(s, h):
    pr = " "
    s = f"{s}{pr}{h}"
    return s


def mk(s, h, kl):
    pr = " "
    s = f"{s}{pr}{kl}-{h}"
    return s


def ms(x1):
    x1 = x1.split()
    st = ""
    k = ""

    for i in range(len(x1)):
        if i == len(x1)-1:
            if k == "":
                st = m(st, x1[i])
            else:
                st = mk(st, x1[i], k)

        elif int(x1[i+1]) - int(x1[i]) == 1:
            if k == "":
                k = x1[i]

        else:
            if k == "":
                st = m(st, x1[i])+","

            else:
                st = mk(st, x1[i], k)+","
                k = ""
    return st


x = input("Enter the ordered list without duplicates in format : 4 5 10 20 ")
print(len(x))
print(ms(x))
