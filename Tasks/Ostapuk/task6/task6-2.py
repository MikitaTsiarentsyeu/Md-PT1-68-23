def palindrom(str):
    if str[0] != str[-1]:
        return 'NO'
    elif len(str) == 1:
        return 'YES'   
    elif str[0] == str[-1]:
        if len(str) == 2:
            return 'YES'
        else:   
            return palindrom(str[1:-1]) 
str = str(input('Enter the word: ')).lower()
print(palindrom(str))