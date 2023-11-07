def read():
    '''This function reads a file and returns its contents as a string'''
    try:
        with open("Task_2.txt", 'r') as f:
            return (f.read())
    except FileNotFoundError:        
        return (f'File not found')
print(read())



