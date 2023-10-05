# for i in range(1, 101):
#     res = ""
#     if i % 3 == 0:
#         res += "fizz"
#     if i % 5 == 0:
#         res += "buzz"
#     if not res:
#         res = i

#     print(res)

print([("fizz"*(i%3==0)+"buzz"*(i%5==0)) or i for i in range(1, 101)])