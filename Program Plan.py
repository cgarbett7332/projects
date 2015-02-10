import RPi.GPIO as GPIO
import time
import math

windpin = 17
windcount = 0

def spin(channel):
    global windcount
    windcount +=1
    print (windcount)

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
    print (raincount * 0.2794)

GPIO.setmode(GPIO.BCM)
GPIO.setup(rainpin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(rainpin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)

input("Press Enter to start...")
while True:
    count = 0
    time.sleep(3)
    print (raincount *0.2794)
    print (windcount)
