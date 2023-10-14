import os
old_dir = os.getcwd()
os.chdir("../../!!!Tasks/Task4")

with open("text.txt") as f:
    os.chdir(old_dir)
    old_list = f.readline().replace(".", " ").strip().replace(",", " ").replace("  ", " ").split(" ")
print(old_list)

def reversed_order(x: list):

    new_list = []

    for i in x:
        rev_str = ""   
        for j in i:
            rev_str = j + rev_str
        new_list.append(rev_str)
        
    return new_list

print(reversed_order(old_list))