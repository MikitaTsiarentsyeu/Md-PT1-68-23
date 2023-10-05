vow = ['a', 'e', 'o', 'i', 'u', 'y']
st = str(input("Enter the string:"))
i = 0
for i in range(len(vow)):
    st = st.replace(vow[i], '')
print("The string without vowels:", st)
