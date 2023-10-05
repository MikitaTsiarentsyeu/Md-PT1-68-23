st = str(input("Enter the string:"))
st = st.split()
dict1 = {}
i = 0
j = 0
for i in range(len(st)):
    k = 0
    for j in range(len(st)):
       if st[i] == st[j]:
           k += 1
    dict1.setdefault(st[i], str(k))
print(dict1)
