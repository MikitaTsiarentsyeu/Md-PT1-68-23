t = str(input("Please enter the time in the format hh:mm: "))
if len(t) > 5:
    print("Incorrect format.")
    exit()

t = t.split(":")
hh = int(t[0])
min = int(t[1])

if hh > 25 or min > 60:
    print("Incorrect format.")
    exit()

m0 = {1: "час",
      2: "два",
      3: "три",
      4: "четыре",
      5: "пять",
      6: "шесть",
      7: "семь",
      8: "восемь",
      9: "девять",
      10: "десять",
      11: "одиннадцать",
      12: "двенадцать",
      13: "час",
      14: "два",
      15: "три",
      16: "четыре",
      17: "пять",
      18: "шесть",
      19: "семь",
      20: "восемь",
      21: "девять",
      22: "десять",
      23: "одиннадцать"}

m30 = {0: "первого",
       1: "второго",
       2: "третьего",
       3: "четвертого",
       4: "пятого",
       5: "шестого",
       6: "седьмого",
       7: "восьмого",
       8: "девятого",
       9: "десятятого",
       10: "одиннадцатого",
       11: "двенадцатого",
       12: "первого",
       13: "второго",
       14: "третьего",
       15: "четвертого",
       16: "пятого",
       17: "шестого",
       18: "седьмого",
       19: "восьмого",
       20: "девятого",
       21: "десятятого",
       22: "одиннадцатого",
       23: "двенадцатого"}

mm = {1: "одна",
      2: "две",
      3: "три",
      4: "четыре",
      5: "пять",
      6: "шесть",
      7: "семь",
      8: "восемь",
      9: "девять",
      10: "десять",
      11: "одиннадцать",
      12: "двенадцать",
      13: "тринадцать",
      14: "четырнадцать",
      15: "пятнадцать",
      16: "шестнадцать",
      17: "семнадцать",
      18: "восемнадцать",
      19: "девятнадцать",
      20: "двадцать",
      30: "тридцать",
      40: "сорок"}

dm = {59: "одной",
      58: "двух",
      57: "трех",
      56: "четырех",
      55: "пяти",
      54: "шести",
      53: "семи",
      52: "восьми",
      51: "девяти",
      50: "десяти",
      49: "одиннадцати",
      48: "двенадцати",
      47: "триннадцати",
      46: "четырнадцати",
      45: "пятнадцати"}



if min == 00:
    if hh == 1 or hh == 13:
        print(m0[hh] + " " + "ровно")
    elif 1 < hh < 5 or 13 < hh < 17:
        print(m0[hh] + " " + "часа ровно")
    elif 5 <= hh <= 12 or 14 <= hh <= 23:
        print(m0[hh] + " " + "часов ровно")
    else:
        print(m0[12] + " " + "часов ровно")
if min == 30:
    if 0 <= hh <= 23:
        print("половина" + " " + m30[hh])
if min == 1:
    print(mm[min] + " " + "минута" + " " + m30[hh])
if 1 < min < 5:
    print(mm[min] + " " + "минуты" + " " + m30[hh])
if 5 <= min <= 20:
    print(mm[min] + " " + "минут" + " " + m30[hh])
if min == 21 or min == 31 or min == 41:
    print(mm[min-1] + " " + mm[1] + " " + "минута" + " " + m30[hh])
if 22 <= min < 25 or 32 <= min < 35 or 42 <= min < 45:
    print(mm[min - min % 10] + " " + mm[min % 10] + " " + "минуты" + " " + m30[hh])
if 25 <= min < 30 or 35 <= min < 40:
    print(mm[min - min % 10] + " " + mm[min % 10] + " " + "минут" + " " + m30[hh])
if 45 <= min <= 59 and hh < 23:
    print("без" + " " + dm[min] + " " + "минут" + " " + m0[hh+1])
if 45 <= min <= 59 and hh == 23:
    print("без" + " " + dm[min] + " " + "минут" + " " + m0[12])


































