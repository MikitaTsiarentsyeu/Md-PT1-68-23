g = "Напишите программу, которая принимает строку в качестве входных данных и возвращает строку в обратном порядке"
x = ""
for i in g:
    if i in g:
        x += i
print(x[::-1])
