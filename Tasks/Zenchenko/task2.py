#да,я знаю что это шиза,попробую оптимизировать на след неделе(ожидалось что будет проще)
time=input("Введите время в формате: hh:mm")
time=time.replace(" ","")
if time.find(":")=="False":
    print("Неправильная форма ввода")
    exit()
if len(time)<5:
    print("Неправильная форма ввода")
    exit()
time1=time.split(":")
if int(time1[0])>24:
    print("Неправильная форма ввода")
    exit()
if int(time1[1])>59:
    print("Неправильная форма ввода")
    exit()
minute =\
    {
     125:"",00:"ровно",1:"одна",2:"две",3:"три",4:"четыре",5:"пять",6:"шесть",7:"семь",8:"восемь",
     9:"девять",10:"десять",11:"одинадцать",12:"двенадцать",13:"тринадцать",14:"четырнадцать",
     15:"пятнадцать",16:"шетснадцать",17:"семнадцать",18:"восемнадцать",19:"девятнадцать",
     20:"двадцать",30:"тридцать",40:"сорок",50:"пятьдесят"
     }

hour=\
    {
     24:"двенадцать",0:"",1:"один",2:"два",3:"три",4:"четыре",5:"пять",6:"шесть",7:"семь",8:"восемь",
     9:"девять",10:"десять",11:"одинадцать",12:"двенадцать",13:"тринадцать",14:"четырнадцать",
     15:"пятнадцать",16:"шетснадцать",17:"семнадцать",18:"восемнадцать",19:"девятнадцать",
     20:"двадцать"
     }
hr=\
    {1:"первого",2:"второго",3:"третьего",4:"четвертого",5:"пятого",6:"шестого",7:"седьмого",8:"восьмого",
     9:"девятого",10:"десятого",11:"одинадцатого",12:"двенадцатого"
    }

mn4560=\
    {1:"одной",2:"двух",3:"трех",4:"четырёх",5:"пяти",6:"шести",7:"семи",8:"восьми",
     9:"девяти",10:"десяти",11:"одинадцати",12:"двенадцати",13:"тринадцати",14:"четырнадцати",15:"пятнадцати"
    }


if int(time1[0])>20:
    hour2=(int(time1[0])%10) # _x
    hour1=(int(time1[0])//10)*10 # x_
elif int(time1[0])<21 and int(time1[0])!=00:
    hour2=00
    hour1=int(time1[0])
elif int(time1[0])==00:
    hour2 = 24
    hour1 = 24

if (int(time1[0])>4 and int(time1[0])<21) or int(time1[0])==00:
    hourmark="часов"
elif (int(time1[0])>1 and int(time1[0])<5) or (int(time1[0])>21 and int(time1[0])<25):
    hourmark="часа"
elif int(time1[0])==1 or int(time1[0])==21:
    hourmark="час"

if (int(time1[1])>4 and int(time1[1])<21) or (int(time1[1])>24 and int(time1[1])<31) or \
        (int(time1[1]) > 34 and int(time1[1]) < 41) or (int(time1[1])>44 and int(time1[1])<51) or\
        (int(time1[1])>54 and int(time1[1])<60) or int(time1[1])%10==00:
    minutemark="минут"
elif (int(time1[1])%10>1 and int(time1[1])%10<5):
    minutemark="минуты"
elif int(time1[1])%10==1:
    minutemark="минута"

if int(time1[1])>20 and int(time1[1])<45 :
    minute2=(int(time1[1])%10) # _x
    minute1=(int(time1[1])//10)*10 # x_
elif int(time1[1])<20 and int(time1[1])!=00:
    minute2=125
    minute1=int(time1[1])
elif int(time1[1])==00:
    minute2 = 125
    minute1 = int(time1[1])
elif int(time1[1])>44 and int(time1[1])<60:
    mn=60-(int(time1[1]))
    minute1=mn
    hour2=hour2+1


if int(time1[0]) == 1 or int(time1[0]) == 13:
        hrmark=hr[1+1]
elif int(time1[0]) == 2 or int(time1[0]) == 14:
        hrmark = hr[2+1]
elif int(time1[0]) == 3 or int(time1[0]) == 15:
        hrmark = hr[3+1]
elif int(time1[0]) == 4 or int(time1[0]) == 16:
        hrmark = hr[4+1]
elif int(time1[0]) == 5 or int(time1[0]) == 17:
        hrmark = hr[5+1]
elif int(time1[0]) == 6 or int(time1[0]) == 18:
        hrmark = hr[6+1]
elif int(time1[0]) == 7 or int(time1[0]) == 19:
        hrmark = hr[7+1]
elif int(time1[0]) == 8 or int(time1[0]) == 20:
        hrmark = hr[8+1]
elif int(time1[0]) == 9 or int(time1[0]) == 21:
        hrmark = hr[9+1]
elif int(time1[0]) == 10 or int(time1[0]) == 22:
        hrmark = hr[10+1]
elif int(time1[0]) == 11 or int(time1[0]) == 23:
        hrmark = hr[11+1]
elif int(time1[0]) == 12 or int(time1[0]) == 24 or int(time1[0]) == 00:
        hrmark = hr[1]

if int(time1[1])==00:
    print("Текущее время {} {} {} {}  ".format(hour[hour1], hour[hour2], hourmark, minute[minute1]))
elif int(time1[1])>0 and int(time1[1])<30 or int(time1[1])>30 and int(time1[1])<45  :
    print("Текущее время {} {} {} {} ".format(minute[minute1],minute[minute2],minutemark,hrmark))
elif int(time1[1])==30:
    print("Текущее время пол {} ".format(hrmark))
elif int(time1[1])>44 and int(time1[1])<60:
    print("Текущее время без {} {} {} {}".format(mn4560[minute1], minutemark, hour[hour1], hour[hour2]))


#print ("Текущее время {} {} {} {} {} ".format(hour[hour1],hour[hour2],hourmark,minute[minute1],minute[minute2]))
#print(time1)