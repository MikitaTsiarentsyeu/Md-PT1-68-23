str = 'How are you? what do you think about this course?'
str = str.split()

d_words = {x: str[x] for x in range(len(str))}

print(d_words)
