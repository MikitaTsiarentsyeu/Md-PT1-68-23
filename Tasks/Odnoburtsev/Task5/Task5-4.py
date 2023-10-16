# import os
# old_dir = os.getcwd()
# os.chdir("../../!!!Tasks/Task4")

# with open("text.txt") as f:
#     os.chdir(old_dir)
#     raw_list = f.readline()

raw_list = "The February TIOBE Index of the most popular programming languages is out, and while the work going on in the background of TIOBE calculations has changed, not much has shifted in the way of rankings."

def words_count(x: str):
    """Takes a string and returns numbers of lower and upper case letters in it"""

    print(f"A raw list of strings is:\n{x}\n")
    counter_upper = 0
    counter_lower = 0

    for i in x:
        if i.isalpha() == True:
            if i == i.upper():
                counter_upper += 1
            else:
                counter_lower += 1
    
    print(f"Your string contains {counter_lower} lower case letters \
and {counter_upper} upper case letters")

words_count(raw_list)

