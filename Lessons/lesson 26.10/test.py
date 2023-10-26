import additional as add

print(add, type(add))

print(add.additional_value)

print(dir(add))

# print(additional.test)

print(hasattr(add, "test"))

additional = "test"

print(additional)

add.test = "new attr"
print(add.test)

add.additional_value = add.additional_value + " test"
print(add.additional_value)

print(add.mut)
add.mut.extend("new")
print(add.mut)