st = str(input("Enter the string:"))
st = st.split()
i = 0
ls = []
for i in range(len(st)):
    if len(st[i]) > 5:
        ls.append(st[i])
print('Strings with length more than 5:', ls)
