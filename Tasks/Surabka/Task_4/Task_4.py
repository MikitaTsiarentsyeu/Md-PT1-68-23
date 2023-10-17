limit = int(input('Enter the number greater than 35: '))
if  limit <= 35:
    print('Incorrect number. Try again!')
    exit
else:
    with open ('text.txt', 'r') as f:
        content = f.read()

        words = content.split()
        line = ''
        new_content = []
        for word in words:
            pr_line = str(line)
            line = word if not line else f'{line} {word}'
            if len(line) > limit:
                line = pr_line
                new_content.append(line)
                line = word
            else:
                continue
        
        for i in range(len(new_content)):
            if len(new_content[i]) < limit:
                miss = limit - len(new_content[i]) #недостает символов до размера limit
                nests = new_content[i].count(' ') #количество мест между словами, куда можно поместить пробелы     
                whole = miss // nests #количество пробелов, которое надо добавить в каждый промежуток 
                ostatok = miss % nests #остаток нераспределенных пробелов после распределения по всем промежуткам
                new_content[i] = new_content[i].replace(' ', ' ' * (whole+1)) #распределяем пробелы, полученные от целочисленного деления (умножаем на кол-во плюс 1 (который уже был между словами))
                if ostatok > 0:
                    new_content[i] = new_content[i].replace(' ', ' %', ostatok) #если такой остаток есть, распределяем по одному пробелу такое же количество раз, что и сам остаток(заменяю на пробел плюс %, потому что может между словами уже может быть несколько пробелов, соот-но программа начнет по порядку заменять соседние пробелы)
                new_content[i] = new_content[i].replace('%', ' ') #заменяю обратно % на пробел   
            
        new_content_str = '\n'.join(new_content) + '\n' + line #последний элемент остался в переменной line, поэтому включаю его в строку
            
        with open('text_new.txt', 'w') as f_new:
            f_new.write(new_content_str) 
        print('New text is in the new file text_new.txt') 