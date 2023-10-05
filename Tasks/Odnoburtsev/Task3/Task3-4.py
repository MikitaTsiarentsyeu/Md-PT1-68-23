while True:
    user_input = input("Please enter a list of numbers, e.g. 1.0, 2, 3, etc.:\n")
    user_input = user_input.replace(" ", ",").replace(",,", ",").split(",")
    # user_input = [200, 89, 3, 150, 8, 100, 11, 97, 15, 7, 11, 13, 2, 121, 144, 17, 21]
    
    try:
        new_user_input = []
        for k in range(len(user_input)):
            new_user_input.append(float(user_input[k]))
            
    except:
        print("The values should digits")
        continue
    
    break

# To find the second largest value it's enough to perform only two sorting cycles
def sorting(x):
    for i in range(2):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    print(f"The second largest number in the list you entered is {x[-2]}")

sorting(new_user_input)