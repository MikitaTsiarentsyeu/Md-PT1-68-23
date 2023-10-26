def pw(os=0, num=0, n=-1):
    if num == 0:
        num = int(os)
    if n == -1:
        n = int(input("Enter the power:"))-1
    num = int(num*os)
    n -= 1
    if n == 0:
        return num
    else:
       num = pw(os, num, n)
    return num


nb = int(input("Enter the number:"))
print("The result is:", pw(nb))
