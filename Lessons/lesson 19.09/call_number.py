number = int(input("Enter a number from 0 to 5 to name it:\n"))

if number == 0:
    print("it's zero")
elif number == 1:
    print("it's one")
elif number == 2:
    print("it's two")
elif number == 3:
    print("it's three")
elif number == 4:
    print("it's four")
elif number == 5:
    print("it's five")
else:
    print("idk that number")

if number == 0:
    print("it's zero")
elif number > 0:
    print("it's positive")
else:
    print("it's negative")

if number >= 0:
    if number > 0:
        print("it's positive")
    else:
        print("it's zero")
else:
    print("it's negative")

x = False
print("it's true") if x == True else print("it's false")
# if x == True:
#     print("it's true")
# else:
#     print("it's false")

print("the end")

y = "it's true" if x else "it's false"
print(y)

print("it's positive") if x > 0 else print("it's zero") if x == 0 else print("it's negative")

