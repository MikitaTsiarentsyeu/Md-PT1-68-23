raw_string = "manona"

def reverse_string(x: str):
    if len(x) == 0:
        return
     
    first_char = x[0]
    reverse_string(x[1:])
    print(first_char, end='')

reverse_string(raw_string)