user_input = input("Please enter a list of strings sseparated by commas:\n")
user_input = user_input.replace(" ", "").split(",")

# user_input = ["polsa", "klsjds", "ds", "posdkifos", "qouiwy", "asds", "wieruusa", "sdf", "qwdasasdasdasd", "", "v"]

list_str = []

for i in user_input:
    if len(i) > 5:
        list_str.append(i)
    
print(list_str)
