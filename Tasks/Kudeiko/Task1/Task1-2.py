# 2.Write a program that calculates the area of a circle given its radius,
# ask a user for the radius.

radius = float(input("Please, enter the radius of the circle in centimeter: "))
if radius > 0:
    area_circle = 3.14 * radius ** 2
    print(f'Area of a circle equals: {area_circle:.2f} cm')
else:
    print("Radius of a circle can't be negative or equals zero.")
