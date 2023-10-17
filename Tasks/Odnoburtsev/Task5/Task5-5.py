import random
# raw_list = list(set(random.choices(range(0, 20), k = 20)))

# OR
raw_list = random.sample(range(0, 20), 12)
raw_list.sort()

#OR
# raw_list = [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 17]

def range_finder(x: list):
    """Takes an ordered list of numbers and returns a list of strings
    with ranges for those numbers"""
    
    print(f"A raw list of numbers is:\n{x}\n")
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

    def list_to_str(y: list):
        """Takes a list of strings with ranges of numbers and
        returns a string with ranges of numbers"""

        str = ", ".join(y)
        print(f"A string with ranges of numbers is:")
        
        return repr(str)
    
    return list_to_str(new_list)

print(range_finder(raw_list))