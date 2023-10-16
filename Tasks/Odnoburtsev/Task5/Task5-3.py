# import os
# old_dir = os.getcwd()
# os.chdir("../../!!!Tasks/Task4")

# with open("text.txt") as f:
#     os.chdir(old_dir)
#     raw_list = f.readline().replace(".", " ").strip().replace(",", " ").replace("  ", " ").split(" ")

raw_list = "The February TIOBE Index of the most popular programming languages is out, and while the work going on in the background of TIOBE calculations has changed, not much has shifted in the way of rankings."
raw_list = raw_list.replace(".", " ").strip().replace(",", " ").replace("  ", " ").split(" ")

def str_more_5(x: list):
    """Takes a list of strings and returns a list of strings
    each containing more than 5 characters"""
    
    print(f"A raw list of strings is:\n{x}\n")
    new_list = []
    for i in x:
        if len(i) > 5:
            new_list.append(i)
    
    print("A new list of strings each containing more than 5 characters:")
    return new_list

print(str_more_5(raw_list))