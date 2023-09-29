x = input("Enter please test string: ")
VOWELS = "aeiouyауоыэяюёие" # Vowels of the Russian and English alphabet
y = 0
for i in x.lower():
    if i in VOWELS:
        y += 1
print(y)