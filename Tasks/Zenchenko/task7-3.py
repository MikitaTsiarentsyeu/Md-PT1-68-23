def sum_dev_2(lst):
    lst = lst.strip()
    lst = lst.split(" ")
    sum_1 = 0
    for i in range(len(lst)):
        try:
            if 0 == int(lst[i]) % 2:
                sum_1 = sum_1 + int(lst[i])
        except ValueError:
            return "Invalid input"
    return sum_1


list1 = input("Enter the list of int in format: 10 9 8 7 6 5\n")
print(sum_dev_2(list1))
