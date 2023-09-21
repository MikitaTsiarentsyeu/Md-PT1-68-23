s = "test literal"
s2 = 'another literal'
s3 = """another
another
literal"""

print(type(s))
print(str(45))
print(45)
print(str(print))

print(repr(''))
print(repr(' '))
print(repr('\n'))
print(repr(str(45)))
print(repr(45))

s = "my very long string"
print(len(s))
print(s[0], s[1], s[2], s[3])
print(s[-1], s[-2], s[-3])
# print(s[150]) error

print(s[len(s)-1])

# s[0] = "t" error

print(s[3:7])
print(s[0:len(s)])
print(s[3:-3])
print(s[2:8:2])
print(s[::-1])

print("t" in s)
print("str" in s)
print("g s" in s)
print("stru" in s)

print(s.find("v"))
print(s.find("str"))
print(s.find(" "))
print(s.count(" "))
print(s.find("test"))

print(s.replace(" ", "_"))
print(s)
s = s.replace(" ", "_")
print(s)

# s = s.replace(" ", "_")
# s = s.replace("string", "str")
# s = s.replace("m", "M")
s = s.replace(" ", "_").replace("string", "str").replace("m", "M")
print(s)

print(s.upper())
print(s)
s = s.lower()
print(s)
s = s.capitalize()
print(s)

print(5+5)
print('5'+'5')
print("test " + "str")

print("test"*10)

s = "   very important data  "
# s = s.replace("  ", "")
# print(s)
s = s.strip()
print(repr(s))

coords = "3, -6, 12"
print(coords.split())
print(coords.replace(' ', '').split(','))

coords = coords.replace(' ', '').split(',')
print('!@#$%^&*()'.join(coords))
print(':'.join(coords))


c, d, p = "cat", "dog", "parrot"
"a cat, a dog, and a parrot"
animals = "a " + c + ", a " + d + ", and a " + p
print(animals)
"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog, and a"
"a cat, a dog, and a parrot"

res = f"a {c}, a {d}, and a {p}"
print(res)

answer = 25
print(f"the answer is {answer}")

print("a {}, a {}, and a {}".format(c, d, p))

# print("kjrk %s" % "TEST") old way, never use it