while True:
    user_query = input("Please enter a list of integers:\n")
    user_query = user_query.replace(" ", ",").replace(",,", ",").split(",")
    # user_query = [89, 3, 8, 100, 11, 97, 15, 7, 11, 13, 2, 121, 144, 17, 21]

    try:
        user_input = []
        for k in range(len(user_query)):
            user_input.append(int(user_query[k]))
    except:
        print("The numbers should be integers")
        continue
    
    break

result_input = []

for i in user_input:
    for j in range(2, int(i)):
        if i%j == 0:
            break
    else:
        result_input.append(i)

if len(result_input) == 0:
    print("Your list doesn't contain any prime numbers.\nTry again")
    exit()

# Because we should extract only maximum it's enough to perform only one sorting cycle 
for l in range(1):
    for m in range(len(result_input)-1):
        if result_input[m] > result_input[m+1]:
            result_input[m], result_input[m+1] = result_input[m+1], result_input[m] 


print(f"The largest prime number is {result_input[-1]}")

