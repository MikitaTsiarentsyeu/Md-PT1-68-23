test_string = ["cat", "python", "damage", "elephant", "dog", "apple", "child", \
"city", "money", "string",]
test_string2 = []
for i in test_string:
    if len(i) > 5:
        test_string2.append(i)
print(test_string2)