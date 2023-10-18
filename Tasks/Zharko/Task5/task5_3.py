def greater(l:list)->list:
    new_l = []
    for i in l:
        if len(i) > 5:
            new_l.append(i)
    return new_l

l = ["one", "two", "dictyonary", "three", "four", "five", "Python", "fourty"]
print(f"Old list: {l}")
print(f"New list with all the strings that have a length greater than 5: {greater(l)}")