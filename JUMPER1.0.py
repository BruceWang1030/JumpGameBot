import threading
import os
#import random


def fun_timer():
    print("Ready to jump, sir")
    os.popen('C:\Tech Project\JUMP JUMP\Color Recognition Feb 16\Color Recognition.py')
    global timer
   # i = random.randint(5,8)
    #print(i)
    timer = threading.Timer(6, fun_timer)
    timer.start()

fun_timer()
