g = "Напишите программу, которая принимает на вход строку и возвращает строку, в которой удалены все гласные"
ls = ["е", "э", "а", "я", "у", "ю", "ы", "и", "о", "ё"]

sl = ""
for i in g:
    if i not in ls:
       sl += i

print(sl)
