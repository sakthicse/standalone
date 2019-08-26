import time
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            time.sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            time.sleep(1)
c1 = Hello()
c2 = Hi()
c1.start()
c2.start()
c1.join()
time.sleep(0.2)
c2.join()
print("End")



		