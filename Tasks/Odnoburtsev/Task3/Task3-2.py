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

def sum_even (x):
    
    sum = 0
    
    for i in x:
        if i % 2 == 0:
            sum += i

    print(f"The sum of all even numbers in the list you entered is {sum}")

sum_even(new_input)
