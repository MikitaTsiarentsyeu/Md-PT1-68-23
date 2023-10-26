import time

start_time = False
is_started = False

def start():
    global start_time, is_started
    is_started = True
    start_time = time.time()

def finish():
    global is_started 
    if is_started:
        current_time  = time.time()
        is_started = False
        return current_time - start_time