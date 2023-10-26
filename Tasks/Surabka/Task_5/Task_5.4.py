def string():
    '''This function returns two numbers: count of lower case letters and count of the upper case letters'''
    lower = [1 for i in str if i.islower()]
    upper = [1 for i in str if i.isupper()]
    return len(lower), len(upper)

str = 'Write a Function that Takes a string as an argument And returns two numbers'
lower, upper = string()
print(lower, upper)