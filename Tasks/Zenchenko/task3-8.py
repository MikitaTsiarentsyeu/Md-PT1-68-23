num = input("Enter the list of numbers:")
num = num.replace(",", " ")
num = num.split()
i = 0
avg = 0
for i in range(len(num)):
    avg += int(num[i])
avg /= len(num)
print('Average value in this list equal to:', avg)
