list = [0, 2, 3, 4, 7, 8, 10]
def task():
    '''This function takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers'''
    start = list[0]
    new_list = []

    for i in range(len(list)-1):
        if list[i] + 1 == list[i+1]:
            continue
        else:
            if start == list[i]:
                new_list.append(f'{list[i]}')
            else: 
                new_list.append(f'{start}-{list[i]}')
            start = list[i+1]       
        
    if list[-2] + 1 == list[-1]:
        new_list.append(f'{start}-{list[-1]}')
    else:
        new_list.append(f'{list[-1]}')
    return (', '.join(new_list))

print(task())