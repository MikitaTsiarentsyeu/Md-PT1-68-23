chunk_size = int(input("Enter maximum number of characters per line(must be greater than 35)"))
if chunk_size < 35:
    print("Wrong input")
    exit()
with open("text.txt", 'r') as f:
    chunk1 = f.read()
    chunk1 = chunk1.replace("\n", "")
    chunk1 = chunk1.strip()
    chunk2 = chunk1.split(" ")
    i = 0
    cl = len(chunk2)
    while i != cl:
        fr = 0
        chunk = ""
        while len(chunk) != chunk_size:
            if i == cl:
                with open("text1.txt", "a") as f1:
                    f1.write(chunk + "\n")
                    print("Formatted text has been writen in text1.txt")
                    exit()
            else:
                chunk = chunk.strip()
                if (len(chunk)+len(chunk2[i]))+1 <= chunk_size:
                    chunk = chunk+" "+chunk2[i]
                    i += 1
                elif len(chunk) + len(chunk2[i]) + 1 > chunk_size and len(chunk) < chunk_size:
                    while True:
                        try:
                            fr = chunk.index(" ", fr+2, len(chunk))
                            break
                        except ValueError:
                            fr = 1
                    chunk = chunk[0:fr]+" "+chunk[fr:len(chunk)]
        with open("text1.txt", "a") as f2:
            f2.write(chunk+"\n")
