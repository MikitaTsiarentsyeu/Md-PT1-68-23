# a, b, c = 3, -14, -5

# D = b*b - 4*a*c

# print(D)

# x1 = (-b+D**0.5)/(2*a)
# x2 = (-b-D**0.5)/(2*a)

# print(x1, x2)

a = float(input("Please enter the a coeff value:\n"))
b = float(input("Please enter the b coeff value:\n"))
c = float(input("Please enter the c coeff value:\n"))

D = b*b - 4*a*c

if D < 0:
    print("there are no roots")
elif D == 0:
    x = -b/(2*a)
    print(x)
else:
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)/(2*a)
    print(x1, x2)