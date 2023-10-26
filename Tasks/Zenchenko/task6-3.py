def vh(str1, s="", i=0, k=0):
    if s == "":
        s = input("Enter the symbol:")
    if str1[i] == s:
        k += 1
    if i == len(str1)-1:
        return k
    else:
        k = vh(str1, s, i+1, k)
    return k


st = input("Enter the string:")
print("The number of occurrences of a given character is:", vh(st))
