import random
position = random.randint(0, 20)

def N_Fibonacci(N):
    """A recursive function to find the Nth number in the Fibonacci sequence"""
    if N == 0 or N == 1:
        return N
    else:
        return N_Fibonacci(N-1) + N_Fibonacci(N-2)
   
print(f"The {position}th number in the Fibonacci sequence is {N_Fibonacci(position)}")