# while True:
#     print("to infinity and beyound!")
# else:
#     print("the end")

x = 1
while x <= 10:
    print(x)
    x += 1


l = list("hfuil")

x = 0
while x < len(l):
    print(l[x])
    x = x + 1
else:
    print("the end")

i = "very important value"

# for i in [1,2,3,4,5]:
#     print(i)

for i in i:
    if i == " ":
        break
    print(i)
else:
    print("the end")

print(i)

l = [1,2,3,4,5]

i = 0
while True:
    if i == 3:
        break
    print(l[i])
    i += 1


# l = [1]
# for i in l:
#     l.append(i)
#     print(l)

for i in "test short string":
    if i == " ":
        continue
    print(i)

for i in "test":
    if i == "t":
        break
else:
    print("the end")

teh_end = False
for i in "test":
    if i == "t":
        teh_end = True
        break

if teh_end:
    print("the end")