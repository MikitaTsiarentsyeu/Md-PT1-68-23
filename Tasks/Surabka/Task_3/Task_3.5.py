s = ['one', 'eleven', 'twelve', 'three', 'thirteen', 'two', 'one hundred']
s_new = []
for i in s:
    if len(i) > 5:
        s_new.append(i)
print(s_new)
