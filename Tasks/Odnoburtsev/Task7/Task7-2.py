import os

def file_reader(file_name: str):
    """Reads a file and returns its contents as a string.
    If the file does not exist returns an error 'FileNotFoundError'"""
    try:
        if os.path.isfile(file_name):
            with open(file_name) as f:
                file_contents = f.read()
                print(file_contents)
        else:
            raise FileNotFoundError(f"The file '{file_name}' is not found in the 'Test7' directory")

    except FileNotFoundError as e:
        print(e)

file_reader("text file.txt")


# The second option:

# def file_reader(file_name: str):
#     try:
#         exist = True
#         f = open(file_name)
#         print(f.read())
#     except FileNotFoundError:
#         exist = False
#         print(f"The file '{file_name}' is not found in the 'Test7' directory")
#     finally:
#         if exist:
#             f.close()

# file_reader("test file.txt")