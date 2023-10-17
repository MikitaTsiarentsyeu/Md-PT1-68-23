# x = 0
# while x < 10:
#     print("test")
#     x += 1

def print_10_times(text, i=0):
    if i == 10:
        return
    print(text)
    print_10_times(text, i+1)

# print_10_times("rec")

# 6! = 6*5*4*3*2*1 = 6*5!
# 5! = 5*4*3*2*1 = 5*4!
# 4! = 4*3*2*1 = 4*3!
# 3! = 3*2*1 = 3*2!
# 2! = 2*1 = 2*1!
# 1! = 1

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

l = [1,2,[5,7,[9,7,[1,],5],8],3,4]

# for i in l:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j, list):
#                 for k in j:
#                     print(k)
#                 continue
#             print(j)
#         continue
#     print(i)

def cycle(l):
    for i in l:
        if not isinstance(i, list):
            print(i)
        else:
            cycle(i)

cycle(l)


def digits_sum(num):
    if num == 0:
        return 0
    return (num % 10) + digits_sum(num//10)

print(digits_sum(345))