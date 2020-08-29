import time

start = time.time()
for i in range(10):
    end = time.time()
    time.sleep(1.5)
    print(round((end-start),2))


