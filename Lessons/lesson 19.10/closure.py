
def maker(p):
    def action(n):
        return n**p

    return action

def power(p, n):
    return p**n

print(power(2, 3))

third = maker(3)
print(third(2))

powers = []
for i in range(6):
    powers.append(maker(i))

print(powers)

for power in powers:
    print(power(2))


def maker(sign):
    if sign == "+":
        def action(a, b):
            return a+b
    elif sign == "-":
        def action(a, b):
            return a-b
    elif sign == "*":
        def action(a, b):
            return a*b
    elif sign == "/":
        def action(a, b):
            return a/b
    else:
        return
        
    return action

def maker(sign):
    def action(a, b):
        if sign == "+":
            return a+b
        elif sign == "-":
            return a-b
        elif sign == "*":
            return a*b
        elif sign == "/":
            return a/b
        else:
            return
        
    return action

sum = maker('+')
print(sum(2, 3))

print(maker('*')(2, 3))