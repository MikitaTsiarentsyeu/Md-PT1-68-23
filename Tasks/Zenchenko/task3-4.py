num = input("Enter the list of numbers:")
num = num.replace(",", " ")
num = num.split()
i = 0
for i in range(len(num)):
    num[i] = int(num[i])
mx1 = max(num)
while mx1 in num != True:
    num.remove(max(num))
mx2 = max(num)
print('The second largest number in the list is:', mx2)
