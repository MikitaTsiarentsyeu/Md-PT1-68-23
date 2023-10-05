# # 4. Write a program that takes a list of numbers as input and
# # returns the second largest number in the list.


def seq_largest_num_insertion(lst: list):
    for i in range(len(lst)):
        index = i
        num = lst[i]
        while index > 0 and lst[index-1] > num:
            lst[index] = lst[index-1]
            index -= 1
        lst[index] = num
    return lst[-2]


print(seq_largest_num_insertion(list(map(int, input("Enter numbers separated by spaces:\n").split()))))



