def return_list():
    '''This function takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5'''
    new_list = [i for i in list if len(i) > 5]
    return new_list

list = 'Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.'.replace('.', '').split(' ')
print(f'Original list:\n{list}')
print(f'New list:\n{return_list()}')
