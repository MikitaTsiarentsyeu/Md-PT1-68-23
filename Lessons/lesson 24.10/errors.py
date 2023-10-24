import gc

try:

    while True:
        try:
            x = int(input("enter the x value:"))
            break
        except ValueError:
            print("only integer values are allowed, please try again")
            continue

    while True:
        try:
            y = int(input("enter the positive y value:"))
            if y == 0:
                raise AttributeError("zero value for y is not allowed, please try again")
            if y < 0:
                raise AttributeError("the value should be positive, please try again")
            break
        except ValueError:
            print("only integer values are allowed, please try again")
            continue
        except AttributeError as e:
            print(e)
            continue

    try:
        res = round(x/y)
        print(f"the answer is {res}")
    except ZeroDivisionError:
        print("zero division is not allowed")
    except NameError:
        pass

except:
    print("ooops, something went wrong")
finally:
    del x
    del y
    gc.collect()


# with open("test.txt", 'r') as f:
#     print(f.read())

# try:
#     exist = True
#     f = open("test.txt", 'r')
#     print(f.read())
# except FileNotFoundError:
#     exist = False
# finally:
#     if exist:
#         f.close()