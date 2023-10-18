def reversed_string(a:str)->str:
    new_string = ""
    for i in range(len(a) - 1, -1, -1):
        new_string += a[i]
    return new_string

def reversed_list(l:list)->list:
    new_l = []
    for i in l:
        new_l.append(reversed_string(i))
    return new_l

l = ["one", "two", "three", "four", "five", "Python"]
print(f"Old list: {l}")
print(f"New list: {reversed_list(l)}")