l = input('Enter the integers separated by spaces: ').split()
def convert():
    '''This function produces a list in which numbers are converted to numbers (not strings!), strings are saved as strings'''
    l_2 = []
    for i in l:
        try:
            l_2.append(int(i))
        except ValueError:
            l_2.append(i)
    return l_2
new_list = convert()

def summa():
    '''This function takes a list of integer and returns the sum of all even numbers in the list'''
    sum = 0
    for i in new_list:
        try:
            if i % 2 == 0:
                sum += i
        except TypeError:
            return 'Invalid input type'
    return sum
print(summa())





