# path = r"C:\Drive D\Projects\IT Academy\Python\Md-PT1-68-23\repo\Lessons\lesson 05.10\o_test.txt"
# open(path, 'w')

import os

print(os.getcwd())

path = "test.txt"
with open("test.txt", "r") as f:
    print(f.read())

print(os.name)
levels = ['level 1', 'level 2', 'level 3']
print(os.sep)

new_path = os.sep.join(levels)
print(new_path)

print(os.path.join('level 1', 'level 2', 'level 3'))

# os.makedirs(new_path)
old_cwd = os.getcwd()
os.chdir(new_path)
print(os.getcwd())

open("test.txt", 'w')

# print(os.listdir())
# for item in os.walk(os.getcwd()):
#     print(item)

os.remove("test.txt")
os.chdir(old_cwd)
os.removedirs(new_path)