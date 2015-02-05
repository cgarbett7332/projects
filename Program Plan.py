import RPi.GPIO as GPIO
import time
import math

pin = 17
count = 0

def spin():
    global count
    count +=1
    print (count)

def CalcSpeed():
    radius = 9
    time = 5
    CalcSpeed = ((math.pi*radius)*count)/time
    return CalcSpeed

def speedkmh():
    kms = (CalcSpeed/100000)
    kmh = (kms * 3600)

def loop():
    while True:
        count = 0
        time.sleep(5)
        spin()
        CalcSpeed()
        speedmph()
