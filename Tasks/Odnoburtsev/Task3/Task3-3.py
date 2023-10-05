user_input = "very, very, very, very and and me about me and me about me and and"
# user_input = input("Please enter a phrase with repeated words:\n")
user_input = user_input.replace(" ", ",").replace(",,", ",").split(",")
print(user_input)


def word_counter(x):
    sum_words = {}

# The first option
    for i in x:
        if i in sum_words.keys():
            sum_words.update({i:sum_words[i] + 1})
        else:
            sum_words.update({i:1})

    print(f"The number of each word in the string is {sum_words}")

# The second option
    # for i in x:
    #     counter = 0
    #     for j in x:
    #         if i == j:
    #             counter += 1
    #     sum_words[i] = counter 

    # print(f"The number of each word in the string is {sum_words}")

word_counter(user_input)