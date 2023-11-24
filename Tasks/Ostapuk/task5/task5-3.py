def filter_strings(strings):
    result = []
    for string in strings:
        if len(string) > 5:
            result.append(string)
    return result
strings = ["dogyyyy", "cloo", "greennnn"]
function01 = filter_strings(strings)
print(function01)
