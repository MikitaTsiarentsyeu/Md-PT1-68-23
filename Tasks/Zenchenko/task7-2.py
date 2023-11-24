def f_open(file_name):
    try:
        with open(f"{file_name}.txt", 'r') as f:
            text = f.read()
            return text
    except FileNotFoundError:
        return "File not found"


name = input("Enter file name without . and format:\n")
print(f_open(name))
