def open_file(path_to_file):
    try:
        with open(f"{path_to_file}", 'r') as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print("File not found")


open_file('text7_2.txt')
