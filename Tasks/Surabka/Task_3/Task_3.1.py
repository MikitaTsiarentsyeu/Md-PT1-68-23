s = 'Hello world'
counter = 0
vowels = ['e', 'y', 'u', 'i', 'o', 'a', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']
for i in s:
    if i in vowels:
        counter +=1
print(counter)