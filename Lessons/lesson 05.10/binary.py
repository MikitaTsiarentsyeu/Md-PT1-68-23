import time

start_time = time.time()
print(start_time)
chunk_size = 10000
with open("test.pptx", 'rb') as f:
    with open("test-copy.pptx", 'wb') as new:
        chunk = f.read(chunk_size)
        while chunk:
            new.write(chunk)
            chunk = f.read(chunk_size)

end_time = time.time()
print(end_time)
print("done", end_time-start_time)