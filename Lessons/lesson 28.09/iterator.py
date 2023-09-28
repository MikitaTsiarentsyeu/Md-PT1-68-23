l = [1,2,3,4,5]

# for i in l:
#     print(i)

iterator_object = iter(l)
print(iterator_object, type(iterator_object))

print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))