def rec(str1, k=0, str2=""):
    if k == 0:
        k = len(str1)
    if len(str1) != len(str2):
            str2 = f"{str2}{str1[k-1]}"
            str2 = rec(str1, k-1, str2)
    return str2


s = input("Enter the string:")
print("Reversed string is:", rec(s, 0))
