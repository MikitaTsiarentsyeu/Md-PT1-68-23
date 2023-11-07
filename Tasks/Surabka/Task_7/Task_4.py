import time

def write_function(func):
    def wrapper(n):
        start = time.time()
        res = func(n)
        finish = time.time()
        with open ('Task_4.txt', 'w') as f:
            result = f'The execution time is {finish-start}\nThe argument is n = {n}\nThe return value of a function is {res}.'
            f.write(result)
        return result 
    return wrapper

@write_function
def generate_fizz_buzz_list(n):
    return ['FizzBuzz' if i % 15 == 0 else 'Fizz'if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, n+1)]
generate_fizz_buzz_list(100000)
# print(r)


    
    






