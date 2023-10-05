str = 'hello world мой маленький друг'
volwes = 'eyuioaEYUIOAуеыаоэяиюёУЕЫАОЭЯИЮЁ'

res_str = ''

for letter in str:
    if not letter in volwes:
        res_str += letter

print(res_str)
