string = input("Enter the text(EN): ")
volwes = "aeiouy"
d_string = " "
for i in string:
    if not i in volwes:
        d_string += i    
print(d_string)