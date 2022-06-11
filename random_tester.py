# A Simulator for randomness and how does it close up to 0.5

import time
from random import random
from math import fabs

def rand():
    bestavgs = []
    avg = 0
    enu = 0
    num = 0
    bestavg = 0

    while True:
        time.sleep(0.0001) # Puts a limit on its CPU-consumption
        num = random() 
        avg *= enu 
        enu += 1
        avg += num
        avg /= enu
        if fabs(avg - 0.5) <= fabs(bestavg - 0.5):
            bestavgs.append(avg)
            bestavg = avg
            print(bestavg, enu, sep='   ')

if __name__ == '__main__':
    rand()
