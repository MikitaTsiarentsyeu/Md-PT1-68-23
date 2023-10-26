# def func(str):
#     if len(str) > 0:
#         print(str[-1], end = '')
#         func(str[:-1])
# str = 'Write a function'
# func(str)



def func(str):
    '''This recursive function reverses a string'''
    if len(str) == 1:
        return str[0]    
    print(str[-1], end = '')
    return func(str[:-1])
str = 'Write a function'
print(func(str))