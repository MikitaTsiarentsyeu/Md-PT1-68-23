def input_number(number: str):
    if not number.isdigit:
        exit('Please enter a valid number')
    elif int(number) <= 35:
        exit('Please enter a valid number greater than 35')
    return int(number)


def lenth_chunk(chunk, chunk_size):
    if len(chunk) != chunk_size and '\n' not in chunk:
        while len(chunk) != chunk_size:
            chunk = chunk.replace(' ', '  ', chunk_size - len(chunk))
            if len(chunk) != chunk_size:
                chunk = chunk.replace('  ', '   ', chunk_size - len(chunk))
    return chunk


chunk_size = input_number(input("Enter a whole natural number greater than 35:\n"))
pos_curs = 0
with open("text.txt", 'r') as f:
    chunk = f.read(chunk_size + 1)
    while chunk:
        if '\n' in chunk:
            chunk = chunk[:chunk.find('\n')] + '\n'
            pos_curs += len(chunk) + 1
            f.seek(pos_curs)
        elif len(chunk) < chunk_size:
            pass
        elif (chunk[-2].isalpha() and (chunk[-1].isalpha() or chunk[-1] in ["'", '"', ".", ","])) or (
                chunk[-2] == '"' and chunk.count('"') < 2):
            chunk = chunk[:chunk.rfind(' ')]
            pos_curs += len(chunk) + 1
            f.seek(pos_curs)
        elif (chunk[-2] in ['+', '#', "'"] and chunk[-1] != ' ') or (chunk[-2].isdigit() and chunk[-1].isdigit()):
            chunk = chunk[:chunk.rfind(' ')]
            pos_curs += len(chunk) + 1
            f.seek(pos_curs) + 1
        elif chunk[-2] == ' ':
            chunk = chunk[:-2]
            pos_curs += len(chunk) + 1
            f.seek(pos_curs)
        elif chunk[-2] in [',', '.']:
            chunk = chunk[:-1]
            pos_curs += len(chunk) + 1
            f.seek(pos_curs)
        elif chunk[-1] == ' ':
            chunk = chunk[:-1]
            pos_curs += len(chunk) + 1
            f.seek(pos_curs)

        fin_chunk = lenth_chunk(chunk, chunk_size)

        with open("text_1.txt", "a") as d:
            d.write(fin_chunk if '\n' in fin_chunk else fin_chunk + '\n')

        chunk = f.read(chunk_size)
