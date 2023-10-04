while True:
    user_input = input("Please enter a list of numbers:\n")
    user_input = user_input.replace(" ", ",").replace(",,", ",").split(",")

    try:
        new_input = []
        for k in range(len(user_input)):
            new_input.append(float(user_input[k]))
            
    except:
        print("The values should digits")
        continue

    break

m = 0
for i in new_input:
    m += i

mean_value = m / len(new_input)
print(f"The mean value is {mean_value}")