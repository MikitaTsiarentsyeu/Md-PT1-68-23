

def change_array(array):
    x = 0
    new_array = []
    for i in array:
        if x + len(i) < 5:
            new_array.append(i)
            print(new_array,'\n')
            new_array.append(i)


    return new_array


