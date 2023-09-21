t = (1,2,3,4,5,"test")
print(type(t), t)

t = ()
print(type(t), t)

t = (1,)
print(type(t), t)

t = (1,2,3,4,5,"test")
print(t[0], t[::-1], (1,2,3)+(0,)*3)

# t[0] = 1.0 error

# t.append(10) error

print(len(t))

del t