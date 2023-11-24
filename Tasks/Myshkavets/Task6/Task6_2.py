def is_palindrome(s):
    if len(s) <= 1:
        return True
    first_char = s[0].lower()
    last_char = s[-1].lower()
    if first_char.isalnum() and last_char.isalnum():
        if first_char == last_char:
            return is_palindrome(s[1:-1])
    return False

input_string = "A man, a plan, a canal, Panama"
result = is_palindrome(input_string)
if result:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
