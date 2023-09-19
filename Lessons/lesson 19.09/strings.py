print(ord('a'))
print(ord('A'))
print(ord('а'))
print(ord('А'))

"test"
print(ord('t'), ord('e'), ord('s'), ord('t'))

for i in range(1, 10001):
    print(chr(i), end=' ')

print("test" == 'test' == """test""" == '''test''')

x = """this is 
a comment 
on its own"""
print(x)

print("A" == "А")