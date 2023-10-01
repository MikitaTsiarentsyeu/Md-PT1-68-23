num = input("Enter the list of numbers:")
num = num.replace(",", " ")
num = num.split()
i = 0
max1 = 0

for i in range(len(num)):
    if int(num[i]) <= 1:
        continue
    k = 0
    for j in range(2, int(int(num[i])**0.5) + 1):  #j = корень числа+1 => если число не простое, то % J == 0 будет True

        if int(num[i]) % j == 0:
            k = k + 1

    if k == 0 and int(num[i]) > max1:
        max1 = int(num[i])

if max1 == 0:
    print('There is no prime numbers')
else:
    print('The largest prime number is:', max1)
