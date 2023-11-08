def count_occurrences(string, character):
    if len(string) == 0:
        return 0
    elif string[0] == character:
        return 1 + count_occurrences(string[1:], character)
    else:
        return count_occurrences(string[1:], character)
s = "hello world"
c = "l"
print(count_occurrences(s, c))