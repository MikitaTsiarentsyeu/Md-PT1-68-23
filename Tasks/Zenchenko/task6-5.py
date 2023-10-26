def fib(n, past=0, num=1):
    if n != 2:
        s = num
        num = past + num
        past = s
        n -= 1
        num = fib(n, past, num)

    else:
        return num
    return num


nb = int(input("Enter the number:"))
print("The result is:", fib(nb))
