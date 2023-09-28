
while True:
    user_input = input("Input your value in format hh:mm\n")

    if len(user_input) != 5:
        print("incorrect value length, please try again")
        continue

    if user_input[2] != ':':
        print("incorrect value without ':', please try again")
        continue

    values = user_input.split(':')
    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("incorrect value of hours or minutes, it should be digits, please try again")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 23 or minutes > 59:
        print("incorrect value of hours or minutes, it's too big, please try again")
        continue

    break

print("the main logic goes here")