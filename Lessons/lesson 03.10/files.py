
with open("test.txt", "w") as f:
    print(f, type(f))
    f.write("test content from 'w' mode\n")
    f.write("another test writing\n")

with open("test.txt") as f:
    print(f, type(f))
    print(f.read())
    f.seek(0)
    lines = f.readlines()

print(lines)

with open("test-copy.txt", "w") as f:
    f.writelines(lines)

with open("test-copy.txt", "a") as f:
    f.write("hello from 'a' mode")