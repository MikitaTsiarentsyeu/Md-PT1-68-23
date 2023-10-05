num = input("Enter the list of numbers:")
num = num.replace(",", " ")
num = num.split()
i = 0
sum1 = 0
for i in range(len(num)):
    sum1 = sum1+int(num[i])
print("The sum of all numbers equal to:", sum1)
