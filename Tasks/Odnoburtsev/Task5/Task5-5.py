import random
# old_list = list(set(random.choices(range(0, 20), k = 20)))
old_list = random.sample(range(0, 20), 12)
old_list.sort()

# old_list = [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 17]

def range_finder(x: list):
    print(x)
    counter = 0
    new_list = []

    for i in range(len(x)-1):
            
        if x[i+1] - x[i] == 1:
            counter += 1          
            continue        
        else:
            if counter == 0:
                new_list.append(f"{x[i]}")
            else:
                new_list.append(f"{x[i-counter]}-{x[i]}")
            counter = 0

    if counter == 0:
        new_list.append(f"{x[i+1]}")
    else:
        new_list.append(f"{x[i-counter+1]}-{x[i+1]}")

    str = ", ".join(new_list)
    return str

print(repr(range_finder(old_list)))