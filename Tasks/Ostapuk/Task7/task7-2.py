def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "File not found"

file_path = 'example.txt'

result = read_file_contents(file_path)
print(result)


