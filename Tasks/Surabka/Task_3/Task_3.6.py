s = 'Hello world'
s_new = ''
vowels = ['e', 'y', 'u', 'i', 'o', 'a', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']

for i in s:
    if i not in vowels:
        s_new += i 
print(s_new)