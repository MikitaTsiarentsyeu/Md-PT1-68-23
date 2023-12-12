def read_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

# Example usage:
contents = read_file_contents('example.txt') # Replace 'example.txt' with your file path
print(contents)