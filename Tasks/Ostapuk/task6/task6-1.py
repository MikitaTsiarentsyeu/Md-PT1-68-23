def func(str):
    if len(str) == 1:
        return str[0]    
    print(str[-1], end = '')
    return func(str[:-1])
str = 'monkeys love bananas'
print(func(str))