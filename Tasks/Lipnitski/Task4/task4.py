import os
# Data validation
while True:
    chunk_size = input(
        "Please enter a parameter maximum number of characters per line, which must be greater than 35:\n")

    try:
        chunk_size = int(chunk_size)
    except:
        print("The value entered must be a integer number")
        continue

    if chunk_size <= 35:
        print("The number must be greater than 35")
        continue
    break

with open('text.txt', 'r') as f:
    content = f.read()

words = content.split()
limit = chunk_size - 1
line = ''
with open('text_new.txt', 'w') as new_f:
    for word in words:
        pr_line = str(line)
        line = word if not line else f'{line} {word}'

        if len(line) > limit:
            miss = int(limit) - int(len(pr_line))
            spaces = pr_line.count(' ')
            whole = (miss//spaces) + 1
            counter = 0
            if miss == 0:
                pr_line
            elif miss < spaces:
                counter = miss
            elif miss >= spaces:
                whole -= 1
                counter = spaces

            spaces_to_replace = ' ' + ' ' * whole
            pr_line = pr_line.replace(' ', spaces_to_replace, counter)

            new_f.write(f'{pr_line}\n')
            line = word
        else:
            continue
    print('Created text_new.txt with formated text')
