# 2. Write a recursive function to check whether a given string is a palindrome.

def find_palindrom(palindrom: str):
    if not len(palindrom):
        return "Word being tested - polydrome"
    if palindrom[0].lower() == palindrom[-1].lower():
        return find_palindrom(palindrom[1:-1])
    return "The word being tested is not a polydrome"


print(find_palindrom(input("Enter the word to be checked:\n")))