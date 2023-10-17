incomingtext = input("enter the text:")
volwes = {
    'A': 'a',
    'E': 'e',
    'I': 'i',
    'O': 'o',
    'U': 'u',
    'Y': 'y',
    'a': 'a',
    'e': 'e',
    'i': 'i',
    'o': 'o',
    'u': 'u',
    'y': 'y',
}
count = 0
for i in incomingtext:
    if i in volwes:
        count += 1
print(count, "number of vowels") 