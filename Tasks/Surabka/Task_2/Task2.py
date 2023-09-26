t = str(input("Please enter the time in the format hh:mm: "))
if len(t) > 5:
    print('Incorrect date format. Try again!')
    exit()

t = t.split(':')
hh = t[0]
min = t[1]

if hh > '25' or min > '60':
    print('Incorrect date format. Try again!')
    exit()

d_hh = {
    '00' : 'первого',
    '01' : 'второго',
    '02' : 'третьего',
    '03' : 'четвертого',
    '04' : 'пятого',
    '05' : 'шестого',
    '06' : 'седьмого',
    '07' : 'восьмого',
    '08' : 'девятого',
    '09' : 'десятого',
    '10' : 'одинадцатого',
    '11' : 'двенадцатого',
    '12' : 'первого',
    '13' : 'второго',
    '14' : 'третьего',
    '15' : 'четвертого',
    '16' : 'пятого',
    '17' : 'шестого',
    '18' : 'седьмого',
    '19' : 'восьмого',
    '20' : 'девятого',
    '21' : 'десятого',
    '22' : 'одинадцатого',
    '23' : 'двенадцатого',
    '24' : 'первого', 
}
d_hh_for_min_45_59 = {
    '00' : 'час',
    '01' : 'два',
    '02' : 'три',
    '03' : 'четыре',
    '04' : 'пять',
    '05' : 'шесть',
    '06' : 'семь',
    '07' : 'восемь',
    '08' : 'девять',
    '09' : 'десять',
    '10' : 'одинадцать',
    '11' : 'двенадцать',
    '12' : 'час',
    '13' : 'два',
    '14' : 'три',
    '15' : 'четыре',
    '16' : 'пять',
    '17' : 'шесть',
    '18' : 'семь',
    '19' : 'восемь',
    '20' : 'девять',
    '21' : 'десять',
    '22' : 'одинадцать',
    '23' : 'двенадцать',
    '24' : 'час', 
}
d_hh_for_min_0 = {
    '00' : 'двенадцать часов',
    '01' : 'час',
    '02' : 'два часа',
    '03' : 'три часа',
    '04' : 'четыре часа',
    '05' : 'пять часов',
    '06' : 'шесть часов',
    '07' : 'семь часов',
    '08' : 'восемь часов',
    '09' : 'девять часов',
    '10' : 'десять часов',
    '11' : 'одинадцать часов',
    '12' : 'двенадцать часов',
    '13' : 'час',
    '14' : 'два часа',
    '15' : 'три часа',
    '16' : 'четыре часа',
    '17' : 'пять часов',
    '18' : 'шесть часов',
    '19' : 'семь часов',
    '20' : 'восемь часов',
    '21' : 'девять часов',
    '22' : 'десять часов',
    '23' : 'одинадцать часов',
    '24' : 'двенадцать часов', 
}
d_min = {
    '01' : 'одна минута',
    '02' : 'две минуты',
    '03' : 'три минуты',
    '04' : 'четыре минуты',
    '05' : 'пять минут',
    '06' : 'шесть минут',
    '07' : 'семь минут',
    '08' : 'восемь минут',
    '09' : 'девять минут',
    '10' : 'десять минут',
    '11' : 'одинадцать минут',
    '12' : 'двенадцать минут',
    '13' : 'тринадцать минут',
    '14' : 'четырнадцать минут',
    '15' : 'пятнадцать минут',
    '16' : 'шестнадцать минут',
    '17' : 'семнадцать минут',
    '18' : 'восемнадцать минут',
    '19' : 'девятнадцать минут',
    '20' : 'двадцать минут',
    '21' : 'двадцать одна минута',
    '22' : 'двадцать две минуты',
    '23' : 'двадцать три минуты',
    '24' : 'двадцать четыре минуты',
    '25' : 'двадцать пять минут',
    '26' : 'двадцать шесть минут',
    '27' : 'двадцать семь минут',
    '28' : 'двадцать восемь минут',
    '29' : 'двадцать девять минут',
    '31' : 'тридцать одна минута',
    '32' : 'тридцать две минуты',
    '33' : 'тридцать три минуты',
    '34' : 'тридцать четыре минуты',
    '35' : 'тридцать пять минут',
    '36' : 'тридцать шесть минут',
    '37' : 'тридцать семь минут',
    '38' : 'тридцать восемь минут',
    '39' : 'тридцать девять минут',
    '40' : 'сорок минут',
    '41' : 'сорок одна минута',
    '42' : 'сорок две минуты',
    '43' : 'сорок три минуты',
    '44' : 'сорок четыре минуты',
    '45' : 'без пятнадцати минут',
    '46' : 'без четырнадцати минут',
    '47' : 'без тринадцати минут',
    '48' : 'без двенадцати минут',
    '49' : 'без одинадцати минут',
    '50' : 'без десяти минут',
    '51' : 'без девяти минут',
    '52' : 'без восьми минут',
    '53' : 'без семи минут',
    '54' : 'без шести минут',
    '55' : 'без пяти минут',
    '56' : 'без четырех минут',
    '57' : 'без трех минут',
    '58' : 'без двух минут',
    '59' : 'без одной минуты',
}

if '00' < min < '30' or '30' < min < '45':
    print(d_min[min] + ' ' + d_hh[hh])
elif '45' <= min <= '59':
    print(d_min[min] + ' ' + d_hh_for_min_45_59[hh])
elif min == '00':
    print(d_hh_for_min_0[hh] + ' ' + 'ровно')
elif min == '30':
    print('половина' + ' ' + d_hh[hh])


