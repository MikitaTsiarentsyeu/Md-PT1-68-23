input_list = [1, 2, 3, 4, 5, 6, 7, 8]

if not isinstance(input_list, list):
    print("Invalid input type")
else:
    even_sum = 0
    try:
        for number in input_list:
            if isinstance(number, int) and number % 2 == 0:
                even_sum += number
        print(even_sum)
    except TypeError:
        print("Invalid input type")
