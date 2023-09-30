
user_input = input("Please enter a phrase with repeated words:\n")
user_input = user_input.split(" ")

sum_words = {}

# The first option
# k = 1

# for i in user_input:
#     if i in sum_words.keys():
#         sum_words.update({i:k})
#         k += 1
#     else:
#         k += 0
#         sum_words.update({i:k})

for i in user_input:
    counter = 0
    for j in user_input:
        if i == j:
            counter += 1
    sum_words[i] = counter 

print(sum_words)