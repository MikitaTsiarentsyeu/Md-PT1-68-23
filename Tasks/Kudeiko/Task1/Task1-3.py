# 3.Write a program that converts kilometers per hour to meters per second,
# ask a user for the speed.

km_h = int(input("Please, enter the speed in kilometers per hour: "))
if km_h >= 0:
    m_s = km_h / 3.6
    print(f'{km_h} km/h equals {m_s:.1f} m/s')
else:
    print("Speed can't be negative.")
