
with open("test.txt", "w") as f:
    print(f, type(f))
    f.write("test content from 'w' mode\n")
    f.write("another test writing\n")

with open("test.txt", 'r') as f:
    print(f, type(f))
    print(f.read())
    f.seek(0)
    lines = f.readlines()

print(lines)

with open("test-copy.txt", "w") as f:
    f.writelines(lines)

with open("test-copy.txt", "a") as f:
    f.write("hello from 'a' mode\n")

chunk_size = 10
with open("test-copy.txt", 'r') as f:
    chunk = f.read(chunk_size)
    while chunk:
        print(chunk)
        chunk = f.read(chunk_size)

with open("test-copy.txt", "a+") as f:
    f.write("hello from 'a+' mode")
    # print(repr(f.read()))
    print(f.seek(0))
    # print(repr(f.read()))
    f.write("another 'a+' content\n")

with open("test-copy.txt", "r+") as f:
    f.write("new line from 'r+'")
    print(repr(f.read()))
    print(repr(f.read()))

with open("test-copy.txt", "w+") as f:
    f.write("totally new file content")
    print(repr(f.read()))
    f.seek(0)
    f.write("test")
    # print(repr(f.read()))