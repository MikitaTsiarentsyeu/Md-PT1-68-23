import time_it

time_it.start()

for i in range(10000000):
    i+=1

print(time_it.finish())