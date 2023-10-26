def counter(a:str)->int:
    a = a.replace(" ", "")
    xLow, xCap = 0, 0
    for i in a:
        if ord(i) == ord(i.capitalize()):
            xCap += 1
        else:
            xLow += 1
    return xCap, xLow


test_str = "This is string TEST"
print(f"Upper case letters: {counter(test_str)[0]}")
print(f"Lower case letters: {counter(test_str)[1]}")
