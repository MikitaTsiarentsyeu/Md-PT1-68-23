def return_list():
    '''This function takes a list of strings as an argument and returns a new list of strings that are all reversed'''
    new_list = [i[::-1] for i in list]
    return new_list

list = 'Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.'.replace('.', '').split(' ')
print(f'Original list:\n{list}')
print(f'New list:\n{return_list()}')