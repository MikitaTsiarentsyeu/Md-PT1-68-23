def fibonachi(n, a=0, b=1, list=[0, 0]):
    '''This recursive function finds the Nth number in the Fibonacci sequence'''
    if n<=1:
        return list[0]
    else:
        list.append(a + b)
        fibonachi(n-1, a + b , a , list)
        return list[n]
n = int(input('Enter the number more than zero: '))
print(fibonachi(n))
