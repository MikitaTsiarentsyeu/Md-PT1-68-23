def m5(x1):
    z = ""
    k = " "
    x1 = x1.split(" ")
    for i in range(len(x1)):
        if len(x1[i]) > 5:
            z = f"{z}{k}{x1[i]}"
            z = z.strip()
    return z


x = input("Enter strings: ")
print("The strings with length greater than 5 are:", m5(x))
