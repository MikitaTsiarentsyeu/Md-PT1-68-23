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

with open("text.txt") as f:
    chunk = f.read(max + 1)
    with open("result.txt", "w") as g:
        while chunk:
            if "\n" in chunk:
                index = chunk.find("\n")
                len_end = (len(chunk) - 1) - index
                chunk = chunk[:index + 1]
                g.write(chunk)
                f.seek(f.tell() - len_end)
                chunk = f.read(max + 1)
                continue
            if chunk[len(chunk) - 1] != " " and len(chunk) == max + 1:
                chunk = chunk.split()
                f.seek(f.tell() - len(chunk[len(chunk) - 1]))
                del chunk[len(chunk) - 1]
                chunk = ' '.join(chunk)
                c = 1
                while len(chunk) != max:
                    nehvatka = max - len(chunk)
                    chunk = chunk.replace(" " * c, " " + " " * c, nehvatka)
                    c += 1
                g.write(chunk + "\n")
                chunk = f.read(max + 1)
            elif len(chunk) < max + 1:
                g.write(chunk)
                chunk = f.read(max + 1)
            else:
                chunk = chunk[:len(chunk) - 1]
                g.write(chunk + "\n")
                chunk = f.read(max + 1)

input("Text wrote in new file(result.txt) successful!\
 Press Enter for exit.")