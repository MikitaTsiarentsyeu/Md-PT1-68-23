import os
old_dir = os.getcwd()
os.chdir("../../!!!Tasks/Task4")

with open("text.txt") as f:
    os.chdir(old_dir)
    old_list = f.readline()
print(old_list)

def words_count(x: str):
    counter_upper = 0
    counter_lower = 0
    for i in x:
        if i.isalpha() == True:
            if i == i.upper():
                counter_upper += 1
            else:
                counter_lower += 1
    
    return counter_upper, counter_lower

print(f"Your string contains {words_count(old_list)[0]} upper case letters \
and {words_count(old_list)[1]} lower case letters")

