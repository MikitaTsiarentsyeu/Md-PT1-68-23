def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        return "File not found"

file_path = r'C:\Users\Lenovo\Downloads\Python\Pyth\Task7_2.txt'
file_contents = read_file(file_path)

if file_contents == "File not found":
    print("The file was not found.")
else:
    print("File contents:")
    print(file_contents)