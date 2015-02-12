import RPi.GPIO as GPIO
import time
import math
import json

windpin = 17
windcount = 0

def spin(channel):
    global windcount
    windcount +=1
    

def CalcSpeed():
    global windcount
    radius = 9
    time = 5
    CalcSpeed = ((math.pi*radius)*windcount)/time
    return CalcSpeed

def speedkmh():
    kms = (CalcSpeed/100000)
    kmh = (kms * 3600)

GPIO.setmode(GPIO.BCM)
GPIO.setup(windpin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(windpin, GPIO.FALLING, callback=spin, bouncetime=300)

rainpin = 27 #sets pin 27 to pin
raincount = 0

def bucket_tipped(channel):
    global raincount
    raincount += 1
    

GPIO.setmode(GPIO.BCM)
GPIO.setup(rainpin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(rainpin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)

input("Press Enter to start...")
while True:
    count = 0
    time.sleep(5)
    print ("the rain count is: {0}".format(raincount *0.2794))
    print ("the wind count is: {0}".format(windcount))

####################################################################



def StoreRainCount():
    raincount = bucket_tipped(channel)
    raincount.append()
    with open ("raincount.txt",mode='w') as file:
        json.dump(raincount,file)

def StoreWindCount():
    windcount = spin(channel)
    windcount.append()
    with open ("windcount.txt",mode='w') as file:
        json.dump(windcount,file)

StoreRainCount()
StoreWindCount()
