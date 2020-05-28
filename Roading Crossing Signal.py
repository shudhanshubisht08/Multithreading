from threading import *
import time
e= Event()
def trafficpolice():
    while True:
        time.sleep(10)
        print('Traffic police giving GREEN signal')
        e.set()
        time.sleep(10)
        print('traffic police giving RED signal')
        e.clear()

def driver():
    num = 0
    while True:
        print('Drivers waiting for GREEN signal')
        e.wait()
        print('Traffic signal is GREEN....Vehicles can  move')
        while e.isSet():
            num = num + 1
            print('Vehicle NUmber:', num, 'Crossing the sign')
            time.sleep(2)
        print('Traffic signal is RED...Drivers have to wait')


t1 = Thread(target=trafficpolice)
t2 = Thread(target=driver)
t1.start()
t2.start()