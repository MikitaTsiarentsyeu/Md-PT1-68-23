user_input = input("Please enter a list of strings:\n")
user_input = user_input.replace(" ", ",").replace(",,", ",").split(",")

# user_input = ["polsa", "klsjds", "ds", "posdkifos", "qouiwy", "asds", "wieruusa", "832dfgg", "qwdasasdasdasd", "", "v"]

def char_counter(x): 

    list_str = []

    for i in x:
        if len(i) > 5:
            list_str.append(i)
    
    print(f"A list with all strings containing more than 5 characters {list_str}")

char_counter(user_input)