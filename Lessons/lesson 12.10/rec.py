def level1():
    print("start of level 1")
    level2()
    print("end of level 1")

def level2():
    print("\tstart of level 2")
    level3()
    print("\tend of level 2")

def level3():
    print("\t\tstart of level 3")
    level4()
    print("\t\tend of level 3")

def level4():
    print("\t\t\tstart of level 4")
    # level1()
    print("\t\t\tend of level 4")

# level1()

def level(n=1):
    if n == 10:
        return
    print(f"{' '*(n-1)}start of level {n}")
    level(n+1)
    print(f"{' '*(n-1)}end of level {n}")

level()