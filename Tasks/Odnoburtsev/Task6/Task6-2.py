test_string = "ten1net"

def check_palindrome(x: str):
    if not len(x):
        print(f"A string {repr(test_string)} is a palindrome")
        return
     
    first_char = x[0]
    last_char = x[-1]
    if first_char == last_char:
        return check_palindrome(x[1:-1])
          
    else:
        print(f"A string {repr(test_string)} isn't a palindrome")

check_palindrome(test_string)