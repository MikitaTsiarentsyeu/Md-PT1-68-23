import os
old_dir = os.getcwd()
os.chdir("../../!!!Tasks/Task4")

with open("text.txt") as f:
    os.chdir(old_dir)
    old_list = f.readline().replace(".", " ").strip().replace(",", " ").replace("  ", " ").split(" ")
print(old_list)

def str_more_5(x: list):
    new_list = []
    for i in x:
        if len(i) > 5:
            new_list.append(i)
    
    return new_list

print(str_more_5(old_list))