# import os
# old_dir = os.getcwd()
# os.chdir("../../!!!Tasks/Task4")

# with open("text.txt") as f:
#     os.chdir(old_dir)
#     raw_list = f.readline().replace(".", " ").strip().replace(",", " ").replace("  ", " ").split(" ")

raw_list = "The February TIOBE Index of the most popular programming languages is out, and while the work going on in the background of TIOBE calculations has changed, not much has shifted in the way of rankings."
raw_list = raw_list.replace(".", " ").strip().replace(",", " ").replace("  ", " ").split(" ")



def reversed_order(x: list):
    """Takes a list of strings and returns a list of strings
    with a reversed order of letters in the strings"""
    
    print(f"A raw list of strings is:\n{x}\n")
    new_list = []

    for i in x:
        rev_str = ""   
        for j in i:
            rev_str = j + rev_str
        new_list.append(rev_str)
    
    print("A new list of strings with a reversed order of letters:")   
    return new_list

print(reversed_order(raw_list))