vow = ['a', 'e', 'o', 'i', 'u', 'y']
st = str(input("Enter the string:"))
count = 0
i = 0
for i in range(len(st)):
    if st[i] in vow:
        count += 1

print("Count of vowels in string:", count)

