
def reading(a):
    try:
        with open(a) as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"
    
file = "test.txt"
print(reading(file))