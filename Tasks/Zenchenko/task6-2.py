import math


def pol(str1, i=0, k=0, n=0):
    if k == 0:
        k = len(str1)-1
    if str1[n+i] == str1[k-i]:
        if i == math.ceil(k / 2):
            print(True)
            return
        else:
            pol(str1, i+1, k)
    else:
        print(False)
        return


st = input("Enter the string:")
print("Palindrome check:")
pol(st)
