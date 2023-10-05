str = 'hello world мой маленький друг'
volwes = 'eyuioaEYUIOAуеыаоэяиюёУЕЫАОЭЯИЮЁ'

count = 0

for i in str:
    if i in volwes:
        count += 1

print(count)
