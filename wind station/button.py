import RPi.GPIO as GPIO
import time

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

pin_value = GPIO.input(pin)
if pin_value:
    print("HELLO")
