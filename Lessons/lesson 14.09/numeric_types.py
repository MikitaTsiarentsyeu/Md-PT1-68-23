import decimal
import fractions
import math
import random

integer = 10

print(type(integer))

a = 6458675876986790879
b = -54675476675858769878
c = 5645785465316854986465413546849846513512315648648643513213574684351321321385468463546354684685413513548

print(c)

a+b
a-b
a*b
print(type(12/3))


1234567890.1111


print(1/3)

print(0.1+0.1+0.1)

print(round(1.5))
print(round(2.4))
print(round(2.5))
print(round(2.6))
print(round(3.5))
print(round(4.5))
print(round(5.5))
print(round(6.5))

d = decimal.Decimal('3.14')
print(type(d))

print(int(d))
print(d)

print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1'))

# print(decimal.Decimal('0.1')+0.1+0.1) error

print(decimal.Decimal('0.1')+1)

print(fractions.Fraction(0.3))
print(5404319552844595/18014398509481984)

print(fractions.Fraction('0.3'))


print(math.pi)

print(math.sqrt(144))

print(type(math.inf))

print(math.inf+math.inf)

print(0/math.inf)


print(math.nan+100)


print(random.randint(1, 10))