user_query = input("Please enter a list of numbers, e.g. 1.0, 2, 3, etc.:\n")
user_query = user_query.replace(" ", "").split(",")

user_input = []
for k in range(len(user_query)):
    user_input.append(int(user_query[k]))

# user_input = [89.0, 3.0, 8, 100, 11, 97, 15, 7, 11, 13, 2, 121, 144, 17, 21]

result_input = []

for i in user_input:
    for j in range(2, int(i)):
        if i%j == 0:
            break
    else:
        result_input.append(i)

for l in range(len(result_input)-1):
    for m in range(len(result_input)-1):
        if result_input[m] > result_input[m+1]:
            result_input[m], result_input[m+1] = result_input[m+1], result_input[m] 

print(f"The largest prime number is {result_input[-1]}")

