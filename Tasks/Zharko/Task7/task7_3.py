def sum(a):
    try:
        res = 0
        for i in a:
            if i % 2 == 0:
                res += i
        return res
    except TypeError:
        return "Invalid input type"
    
l = [0, 2, 5, 7, 4, 2, 5, 8, 9, 4]
print(sum(l))