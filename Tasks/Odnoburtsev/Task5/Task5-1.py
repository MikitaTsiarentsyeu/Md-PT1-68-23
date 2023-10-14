# The first option
# import random
# def sum_values(a: int, b: int):
#     print(f"The sum of {a} and {b} is equal to:")
#     return a + b

# print(sum_values(random.randint(1, 100), random.randint(1, 100)))

# The second option
first_input = input("Please enter the first integer number:\n")
second_input = input("Please enter the second integer number:\n")

def raw_data(first_input, second_input):
    
    while True:
        try:            
            a, b = int(first_input), int(second_input)

        except ValueError:
            first_input = input("Please enter the first integer number. Try again\n")
            second_input = input("Please enter the second integer number:\n")
            continue

        break

    return a, b

def sum_values(x):
    print(f"The sum of numbers {x[0]} and {x[1]} is equal to")
    return x[0] + x[1]

print(sum_values(raw_data(first_input, second_input)))

# The third option
# def sum_val(user_input):
    
#     while True:
#         try:
#             user_input = user_input.replace(" ", ",").replace(",,", ",").split(",")
#             a, b = int(user_input[0]), int(user_input[1])

#         except ValueError:
#             user_input = input("Please enter two integer numbers. Try again\n")
#             continue
        
#         break
          
#     return print(f"The sum of numbers {a} and {b} is equal to {a+b}")

# sum_val(input("Please enter two integer numbers:\n"))

