with open("text.txt") as f:
    x = f.readlines()

l = []
for i in x:
    y = i.strip().split()
    l += [y]

while True:
    
    max = input("Enter please max count symbols in once string\
(must be greater than 35): ")
    
    if not max.isdigit():
        print("Incorrect value, it should be digits, please try again")
        continue
    
    max = int(max)
    
    if max <= 35:
       print("Incorrect input, must be greater than 35, try again!")
       continue
    
    break

new_text = ""
new_string = ""

for j in l:
    for i in j:
        if not new_string:
            new_string += i
            continue
        
        if len(new_string) + len(i) > max - 1:
            c = 1
            while len(new_string) != max:
                nehvatka = max - len(new_string)
                new_string = new_string.replace(" " * c, " " + " " * c, nehvatka)
                c += 1
            new_text += new_string + "\n"
            new_string = i
        elif len(new_string) + len(i) == max - 1:
            new_text += new_string + " " + i + "\n"
            new_string = ""
        else:
            new_string += " " + i
    
    if new_string:
        new_text += new_string + "\n"
        new_string = ""

with open("result.txt", "w") as f:
    print(f.write(new_text))
input("Text wrote in new file(result.txt) successful!\
 Press Enter for exit.")
