import time
import os
import threading
from mo_test3_2 import CD

T = False

def ABC():
    a = 10
    b = 20
    c = a*b
    for i in range(0,5):
        c = c + CD(a,b)
        print(c+i)
        time.sleep(0.5)
        #if(T):
            #break
    print("End ABC")

def time_time():
    s = time.time()
    for i in range(0,1000):
        t = time.time() - s
        if(t >= 5):
            break
        print(t)
        time.sleep(1)
    print("End time")
    #os._exit(0)
    T = True
    print(T)
    return T

print("start now")

a1 = threading.Thread(target=ABC)
b1 = threading.Thread(target=time_time)

print(T)
a1.start()
b1.start()

print(T)    
print("momo")
b1.join()
print(str(T)+"momo")
a1.join()
print(str(T)+"omom")
