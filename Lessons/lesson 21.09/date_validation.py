dob = input("input your dob in the format dd.mm.yyyy")

dob = dob.replace(' ', '')

if '.' not in dob:
    print("You entered incorect data without a . symbol")
    exit()

if dob.count('.') != 2:
    pass #logic of validation

dob_list = dob.split('.')

# day, month, year = int(dob_list[0]), int(dob_list[1]), int(int(dob_list[2]))
day, month, year = dob_list
day, month, year = int(day), int(month), int(year)

print(day, month, year)